import io
import os
import sys
import tty
import time
import enum
import queue
import atexit
import signal
import cProfile
import threading
import functools
import contextlib

from collections import deque, defaultdict
from dataclasses import dataclass

import pygments.lexers as pl
import pygments.styles as ps


class PubSub:
    def __init__(self):
        self.s = defaultdict(list)

    def sub(self, t, f):
        self.s[t].append(f)

    def pub(self, t, m):
        for f in self.s.get(t, []):
            f(m)


BUS = PubSub()


def esc(d):
    return chr(27) + d


def csi(*args):
    res = '[' + str(args[0])

    for a in args[1:]:
        res += ';'
        res += str(a)

    return esc(res)


def move(x, y):
    return csi(y + 1, x + 1) + 'H'


def retval(v):
    def func():
        return v

    return func


class SigWinch(Exception):
    pass


class Channel:
    def __init__(self):
        self.b = deque()
        self.i = io.FileIO(0, 'r')
        self.o = io.FileIO(1, 'w')
        self.q = queue.SimpleQueue()
        tty.setraw(self.i)
        self.send(csi('?25l'))
        threading.Thread(target=self.runq, daemon=True).start()
        signal.signal(signal.SIGWINCH, self.sigwinch)

    def fini(self):
        os.system('reset')

    def sigwinch(self, *args):
        def err():
            raise SigWinch()

        self.q.put(err)

    def runq(self):
        try:
            while True:
                self.q.put(retval(ord(self.i.read(1))))
        except Exception as e:
            def err():
                raise e

            self.q.put(err)

    def send(self, cmd):
        self.o.write(cmd.encode())

    def recv(self):
        return self.q.get()()

    def next(self):
        try:
            return self.b.popleft()
        except IndexError:
            pass

        return self.recv()

    def read_seq(self, ch):
        while True:
            s = self.recv()

            if s == 27:
                return self.read_to(ch)[1:]

            self.b.append(s)

    def read_to(self, ch):
        res = []

        while True:
            s = self.recv()

            if s == ch:
                return res

            res.append(s)

    def resp(self, ch):
        return ''.join(chr(x) for x in self.read_seq(ord(ch)))

    def dims(self):
        self.send(move(10000, 10000) + csi('6n'))

        y, x = self.resp('R').split(';')

        return int(x), int(y)


KMAP = [
    ('[A', 'up'),
    ('[B', 'down'),
    ('[C', 'right'),
    ('[D', 'left'),
    ('[F', 'end'),
    ('[H', 'home'),
    ('[1~', 'home'),
    ('[2~', 'insert'),
    ('[3~', 'delete'),
    ('[4~', 'end'),
    ('[5~', 'pageup'),
    ('[6~', 'pagedown'),
    ('[7~', 'home'),
    ('[8~', 'end'),
    ('OP', 'f1'),
    ('OQ', 'f2'),
    ('OR', 'f3'),
    ('OS', 'f4'),
    ('[P', 'f1'),
    ('[Q', 'f2'),
    ('[R', 'f3'),
    ('[S', 'f4'),
    ('[15~', 'f5'),
    ('[17~', 'f6'),
    ('[18~', 'f7'),
    ('[19~', 'f8'),
    ('[20~', 'f9'),
    ('[21~', 'f10'),
    ('[23~', 'f11'),
    ('[24~', 'f12'),
]


def make_scan_trie():
    res = {}

    def substr(k):
        s = ''

        for c in k:
            s += c

            yield s

    for k, v in KMAP:
        for sk in substr(k):
            res[sk] = 'int'

        res[k] = v

    return res


def make_ctrl_tables():
    return [(n + 1, 'ctrl-' + chr(ch)) for n, ch in enumerate(range(ord('a'), ord('z')))]


class InputStream:
    TRIE = make_scan_trie()

    ASCII = dict(make_ctrl_tables() + [
        (0, 'ctrl-@'),
        (9, 'tab'),
        (10, 'lf'),
        (13, 'cr'),
        (127, 'bs'),
    ])

    def __init__(self, ch):
        self.ch = ch

    def next(self):
        key = self.ch.next()

        if key < 128:
            if key == 27:
                return self.scan_escape()

            if val := self.ASCII.get(key):
                return val

            if key >= 32:
                return chr(key)

            raise Exception('bad key ' + str(key))

        return self.scan_utf8(key)

    def scan_utf8(self, key):
        runes = [key]

        for i in range(0, 4):
            runes.append(self.ch.next())

            try:
                return bytes(runes).decode()
            except UnicodeError:
                pass

    def scan_escape(self):
        p = ''

        while True:
            p += chr(self.ch.next())

            if v := self.TRIE.get(p):
                if v != 'int':
                    return v
            else:
                raise Exception('unknown escape sequence ' + p)


@dataclass
class Color24:
    r: int
    g: int
    b: int

    def bg(self):
        return csi(48, 2, self.r, self.g, self.b) + 'm'

    def fg(self):
        return csi(38, 2, self.r, self.g, self.b) + 'm'


@dataclass
class Color8:
    n: int

    def bg(self):
        return csi(48, 5, self.n) + 'm'

    def fg(self):
        return csi(38, 5, self.n) + 'm'


def bg4(n):
    if n < 8:
        return csi(40 + n) + 'm'

    return csi(92 + n) + 'm'


def fg4(n):
    if n < 8:
        return csi(30 + n) + 'm'

    return csi(82 + n) + 'm'


TBL4 = [(bg4(x), fg4(x)) for x in range(0, 16)]


@dataclass
class Color4:
    n: int

    def bg(self):
        return TBL4[self.n][0]

    def fg(self):
        return TBL4[self.n][1]


def black():
    return Color4(0)


def white():
    return Color4(15)


@dataclass
class Attrs:
    c: str = None
    b: object = None
    f: object = None

    def fmt(self):
        return self.b.bg() + self.f.fg() + self.c


def combine_attrs(a1, a2):
    return Attrs(c=a2.c or a1.c, b=a2.b or a1.b, f=a2.f or a1.f)


class Async:
    def __init__(self):
        self.q = queue.SimpleQueue()

        threading.Thread(target=self.deq, daemon=True).start()

    def deq(self):
        while True:
            self.q.get()()

    def schedule(self, f):
        self.q.put(f)


def singleton(func):
    @functools.wraps(func)
    def wrapper():
        while True:
            try:
                return func.__result__
            except AttributeError:
                func.__result__ = func()

    return wrapper


@singleton
def asyncmngr():
    return Async()


def schedule(f):
    asyncmngr().schedule(f)


class Display:
    def __init__(self, ch):
        self.ch = ch

        dx, dy = self.ch.dims()

        self.dx = dx
        self.dy = dy
        self.dd = {}

    def flip(self, pixels):
        d = ''
        dd = self.dd
        bp = {}
        dx = self.dx
        dy = self.dy

        for x, y, n in pixels:
            if x >= 0 and x < dx and y >= 0 and y < dy:
                p = x + y * dx

                if pp := bp.get(p):
                    bp[p] = (x, y, combine_attrs(pp[2], n))
                else:
                    bp[p] = (x, y, n)

        for p, (x, y, n) in sorted(bp.items(), key=lambda x: x[0]):
            f = n.fmt()

            if f != dd.get(p):
                dd[p] = f

                d += move(x, y)
                d += f

        schedule(lambda: self.ch.send(d))


class Panel:
    def __init__(self, dx, dy, px):
        self.dx = dx
        self.dy = dy
        self.px = px

    def pixels(self):
        for y in range(0, self.dy):
            for x in range(0, self.dx):
                yield x, y, self.px

    def dispatch(self, ev):
        pass


class Handle:
    def __init__(self, w):
        self.move(0, 0)
        self.w = w

    def pixels(self):
        for x, y, c in self.w.pixels():
            yield x + self.x, y + self.y, c

    def dispatch(self, ev):
        self.w.dispatch(ev)

    def move(self, x, y):
        self.x = x
        self.y = y

        return self


class Composer:
    def __init__(self, ch):
        self.d = Display(ch)
        self.i = InputStream(ch)
        self.o = []
        self.s = dict()

    def add_widget(self, w):
        h = Handle(w)

        self.s[id(h)] = h
        self.o.append(id(h))

        return h

    def loop(self):
        while True:
            def pixels():
                for o in self.o:
                    yield from self.s[o].pixels()

            self.d.flip(pixels())

            c = self.i.next()

            if c == 'ctrl-c':
                raise KeyboardInterrupt()

            self.s[self.o[-1]].dispatch(c)


def parse_color(s):
    if c := s.get('color'):
        return Color24(int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16))

    return white()


class HighLight:
    def __init__(self, p, d):
        self.lex = pl.guess_lexer_for_filename(os.path.basename(p), d)
        self.stl = ps.get_style_by_name('material')
        self.lns = {}

    def style_line_impl(self, l):
        for typ, text in self.lex.get_tokens(l):
            s = parse_color(self.stl.style_for_token(typ))

            for ch in text:
                if ch == '\n':
                    pass
                else:
                    yield ch, s

    def style_line(self, l):
        if len(self.lns) > 10000:
            self.lns.clear()

        while True:
            try:
                return self.lns[l]
            except KeyError:
                self.lns[l] = list(self.style_line_impl(l))

                assert len(l) == len(self.lns[l])


class TextArray:
    def __init__(self, d):
        self.d = d

    def at(self, pos):
        return self.d[pos]

    def delete(self, pos):
        self.d = self.d[:pos] + self.d[pos + 1:]

    def insert(self, pos, c):
        self.d = self.d[:pos] + c + self.d[pos:]

    def x(self, pos):
        return self.xy(pos)[0]

    def y(self, pos):
        return self.xy(pos)[1]

    def xy(self, pos):
        x = 0
        y = 0

        for c in self.d[:pos]:
            if c == '\n':
                x = 0
                y += 1
            else:
                x += 1

        return x, y

    def lines(self):
        return self.d.split('\n')


class Editor:
    def __init__(self, p):
        with open(p) as f:
            d = f.read()

        self.h = HighLight(p, d[:10000])
        self.t = TextArray(d)
        self.c = 0

    @property
    def x(self):
        return self.t.x(self.c)

    @property
    def y(self):
        return self.t.y(self.c)

    def render(self, x1, y1, x2, y2):
        sl = self.t.lines()

        for y in range(y1, min(y2, len(sl))):
            l = self.h.style_line(sl[y])

            for x in range(x1, min(x2, len(l))):
                c, col = l[x]

                if c != ' ':
                    yield x, y, c, col

    def dispatch(self, ev, h):
        if len(ev) == 1:
            self.handle_char(ev)
        else:
            self.handle_event(ev, h)

    def getch(self):
        try:
            return self.t.at(self.c)
        except IndexError:
            return ''

    def key_pagedown(self, h):
        for i in range(0, h):
            self.key_down()

    def key_pageup(self, h):
        for i in range(0, h):
            self.key_up()

    def key_cr(self):
        self.handle_char('\n')

    def key_lf(self):
        self.handle_char('\n')

    def key_home(self):
        self.c -= 1

        while self.getch() not in ('', '\n'):
            self.c -= 1

        self.c += 1

    def key_end(self):
        while self.getch() not in ('', '\n'):
            self.one_right()

    def key_left(self):
        self.c -= 1

        if self.getch() == ' ':
            while self.getch() == ' ':
                self.c -= 1

            self.c += 1

        if self.c < 0:
            self.c = 0

    def one_right(self):
        self.c += 1

    def one_left(self):
        if self.c > 0:
            self.c -= 1

    def key_right(self):
        if self.getch() == ' ':
            while self.getch() == ' ':
                self.c += 1
        else:
            self.one_right()

    def skip_at_max(self, cnt):
        for i in range(0, cnt):
            if self.getch() in ('', '\n'):
                break

            self.one_right()

    def key_up(self):
        x = self.x

        self.key_home()
        self.one_left()
        self.key_home()
        self.skip_at_max(x)

    def key_down(self):
        x = self.x

        self.key_end()
        self.one_right()
        self.skip_at_max(x)

    def key_bs(self):
        self.one_left()
        self.key_delete()

    def key_delete(self):
        self.t.delete(self.c)

    def handle_event(self, ev, h):
        BUS.pub('message', ev)

        def unknown():
            BUS.pub('message', 'unknown: ' + ev)

        func = getattr(self, 'key_' + ev.replace('-', '_'), unknown)

        try:
            func()
        except TypeError:
            func(h)

    def handle_char(self, ch):
        self.t.insert(self.c, ch)
        self.c += 1


class EditorWidget:
    def __init__(self, w, h, e):
        self.e = e
        self.x = 0
        self.y = 0
        self.w = w
        self.h = h
        self.adjust()

    def pixels(self):
        bx = self.x
        by = self.y

        ex = bx + self.w
        ey = by + self.h

        for x, y, c, col in self.e.render(bx, by, ex, ey):
            yield x - bx, y - by, Attrs(c=c, f=col)

        yield self.cx, self.cy, Attrs(b=white())

    @property
    def cx(self):
        return self.e.x - self.x

    @property
    def cy(self):
        return self.e.y - self.y

    def dispatch(self, ev):
        self.e.dispatch(ev, self.h)
        self.adjust()

    def adjust(self):
        while self.cx < 0:
            self.x -= self.w // 2

        while self.cy < 0:
            self.y -= self.h // 2

        while self.cx >= self.w:
            self.x += self.w // 2

        while self.cy >= self.h:
            self.y += self.h // 2


class Rect:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def chars(self):
        yield 0, 0, 0x2553
        yield self.w - 1, 0, 0x2556
        yield self.w - 1, self.h - 1, 0x255C
        yield 0, self.h - 1, 0x2559

        for x in range(1, self.w - 1):
            yield x, 0, 0x2500
            yield x, self.h - 1, 0x2500

        for y in range(1, self.h - 1):
            yield 0, y, 0x2551
            yield self.w - 1, y, 0x2551

    def pixels(self):
        for x, y, c in self.chars():
            yield x, y, Attrs(c=chr(c))


@contextlib.contextmanager
def channel():
    ch = Channel()

    try:
        yield ch
    finally:
        ch.fini()


class Label:
    def __init__(self):
        self.t = ''

    def pixels(self):
        for x, c in enumerate(self.t):
            yield x, 0, Attrs(c=c)


def main():
    ed = Editor(sys.argv[1])

    with channel() as ch:
        while True:
            c = Composer(ch)

            w = c.d.dx
            h = c.d.dy

            c.add_widget(Panel(w, h, Attrs(c=' ', b=black(), f=white())))
            c.add_widget(Rect(w, h))

            l = c.add_widget(Label()).move(1, 0).w

            def on_message(m):
                l.t = m

            BUS.sub('message', on_message)

            c.add_widget(EditorWidget(w - 2, h - 2, ed)).move(1, 1)

            try:
                return c.loop()
            except SigWinch:
                pass


try:
    main()
    #cProfile.run('main()')
except KeyboardInterrupt:
    pass
