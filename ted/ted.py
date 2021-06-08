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


class InputStream:
    TRIE = make_scan_trie()

    ASCII = {
        3: 'break',
        127: 'bs',
        10: 'lf',
        13: 'cr',
    }

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


class Attrs:
    def __init__(self, c=None, b=None, f=None):
        self.c = c
        self.b = b
        self.f = f

    def fmt(self):
        return self.b.bg() + self.f.fg() + self.c

    def set_char(self, c):
        self.c = c

        return self

    def set_fg(self, f):
        self.f = f

        return self

    def set_bg(self, b):
        self.b = b

        return self


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
        byp = {}
        dx = self.dx
        dy = self.dy

        for x, y, n in pixels:
            if x >= 0 and x < dx and y >= 0 and y < dy:
                p = x + y * dx

                if pp := byp.get(p):
                    byp[p] = (x, y, combine_attrs(pp[2], n))
                else:
                    byp[p] = (x, y, n)

        for p, (x, y, n) in sorted(byp.items(), key=lambda x: x[0]):
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

            if c == 'break':
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


class Editor:
    def __init__(self, p):
        d = open(p).read()

        self.h = HighLight(p, d)
        self.l = d.split('\n')
        self.x = 0
        self.y = 0

    def render(self, x1, y1, x2, y2):
        sl = self.l

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
            return self.l[self.y][self.x]
        except IndexError:
            return ''

    def skip_ws_right(self):
        while self.getch() == ' ':
            self.x += 1

    def skip_ws_left(self):
        if self.getch() == ' ':
            while self.getch() == ' ':
                self.x -= 1

            self.x += 1

    def key_home(self):
        self.x = 0

    def key_end(self):
        self.x = len(self.l[self.y])

    def key_left(self):
        if self.x == 0:
            if self.y == 0:
                pass
            else:
                self.key_up()
                self.key_end()
        else:
            self.x -= 1
            self.skip_ws_left()

    def key_right(self):
        ch = self.getch()

        if ch == '':
            self.key_down()
            self.key_home()
        elif ch == ' ':
            self.skip_ws_right()
        else:
            self.x += 1

    def key_up(self):
        self.y -= 1

    def key_down(self):
        self.y += 1

    def key_bs(self):
        self.key_left()
        self.key_del()

    def key_del(self):
        l = self.l[self.y]

        self.l[self.y] = l[:self.x] + l[self.x + 1:]

    def handle_event(self, ev, h):
        if ev == 'left':
            self.key_left()
        elif ev == 'right':
            self.key_right()
        elif ev == 'up':
            self.key_up()
        elif ev == 'down':
            self.key_down()
        elif ev == 'pageup':
            self.y -= h
        elif ev == 'pagedown':
            self.y += h
        elif ev == 'home':
            self.key_home()
        elif ev == 'end':
            self.key_end()
        elif ev == 'bs':
            self.key_bs()
        elif ev == 'del':
            self.key_del()

        self.cur_just()

    def cur_just(self):
        self.y = min(self.y, len(self.l) - 1)
        self.y = max(self.y, 0)
        self.x = min(self.x, len(self.l[self.y]))
        self.x = max(self.x, 0)

    def handle_char(self, ch):
        l = self.l[self.y]

        self.l[self.y] = l[:self.x] + ch + l[self.x:]
        self.x += 1


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

        yield self.cx, self.cy, Attrs(c=' ', b=white(), f=white())

    @property
    def cx(self):
        return self.e.x - self.x

    @property
    def cy(self):
        return self.e.y - self.y

    @property
    def hw(self):
        return self.w // 2

    @property
    def hh(self):
        return self.h // 2

    def dispatch(self, ev):
        self.e.dispatch(ev, self.h)
        self.adjust()

    def adjust(self):
        while self.cx < 0:
            self.x -= self.hw

        while self.cy < 0:
            self.y -= self.hh

        while self.cx >= self.w:
            self.x += self.hw

        while self.cy >= self.h:
            self.y += self.hh


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


def main():
    ed = Editor(sys.argv[1])

    with channel() as ch:
        while True:
            c = Composer(ch)

            c.add_widget(Panel(c.d.dx, c.d.dy, Attrs(c=' ', b=black(), f=white())))
            c.add_widget(Rect(c.d.dx, c.d.dy))
            c.add_widget(EditorWidget(c.d.dx - 2, c.d.dy - 2, ed)).move(1, 1)

            try:
                return c.loop()
            except SigWinch:
                pass


try:
    main()
    #cProfile.run('main()')
except KeyboardInterrupt:
    pass
