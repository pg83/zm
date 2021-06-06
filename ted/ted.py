import io
import os
import sys
import tty
import time
import enum
import atexit
import cProfile
import contextlib

from collections import deque
from dataclasses import dataclass


def esc(d):
    return chr(27) + d


def csi(*args):
    return esc('[' + ';'.join(str(x) for x in args))


def move(x, y):
    return csi(y + 1, x + 1) + 'H'


class Channel:
    def __init__(self):
        self.b = deque()
        self.i = io.FileIO(0, 'r')
        self.o = io.FileIO(1, 'w')
        self.init()

    def init(self):
        tty.setraw(self.i)
        self.send(csi('?25l'))

    def fini(self):
        os.system('reset')

    def send(self, cmd):
        self.o.write(cmd.encode('ascii'))

    def recv(self):
        return ord(self.i.read(1))

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
    ('[15~', 'f5'),
    ('[17~', 'f6'),
    ('[18~', 'f7'),
    ('[19~', 'f8'),
    ('[20~', 'f9'),
    ('[21~', 'f10'),
    ('[23~', 'f11'),
    ('[24~', 'f12'),
]


def scan_table():
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
    TRIE = scan_table()

    def __init__(self, ch):
        self.ch = ch
        self.cb = None

    def set_cb(self, cb):
        self.cb = cb

    def read(self):
        res = self.ch.next()

        if self.cb:
            self.cb(res)

        return res

    def next(self):
        key = self.read()

        if key == 27:
            return self.scan_escape()

        if key == 3:
            return 'break'

        if key == 127:
            return 'bs'

        return chr(key)

    def scan_escape(self):
        p = ''

        while True:
            p += chr(self.read())

            if p in self.TRIE:
                v = self.TRIE[p]

                if v == 'int':
                    pass
                else:
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
class Point:
    c: str
    b: object
    f: object

    def fmt(self):
        return self.b.bg() + self.f.fg() + self.c

    def set_char(self, c):
        self.c = c

        return self

    def set_fg(self, c):
        self.f = c

        return self

    def set_bg(self, c):
        self.b = c

        return self


class Display:
    def __init__(self, ch):
        self.ch = ch

        dx, dy = self.ch.dims()

        self.dx = dx
        self.dy = dy
        self.d = ['' for i in range(dx * dy)]

    def flip(self, pixels):
        d = ''
        byp = {}

        for x, y, n in pixels:
            if x >= 0 and x < self.dx and y >= 0 and y < self.dy:
                byp[x + y * self.dx] = (x, y, n.fmt())

        for p, (x, y, f) in byp.items():
            if f != self.d[p]:
                self.d[p] = f

                d += move(x, y)
                d += f

        self.ch.send(d)


class Panel:
    def __init__(self, dx, dy, c):
        self.dx = dx
        self.dy = dy
        self.px = Point(' ', c, c)

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
        self.i = InputStream(ch)
        self.d = Display(ch)
        self.o = []
        self.s = dict()

    def add_widget(self, w):
        h = Handle(w)

        self.s[id(h)] = h
        self.o.append(id(h))

        return h

    def loop(self):
        while True:
            c = self.i.next()

            if c in ('break', 3, chr(3)):
                raise KeyboardInterrupt()

            self.s[self.o[-1]].dispatch(c)

            def pixels():
                for o in self.o:
                    yield from self.s[o].pixels()

            self.d.flip(pixels())


class Editor:
    def __init__(self, d):
        self.l = d.split('\n')
        self.x = 0
        self.y = 0

    def render(self, x1, y1, x2, y2):
        for y in range(y1, min(y2, len(self.l))):
            l = self.l[y]

            for x in range(x1, min(x2, len(l))):
                yield x, y, l[x]

    def dispatch(self, ev, h):
        if len(ev) == 1:
            self.handle_char(ev)
        else:
            self.handle_event(ev, h)

    def handle_event(self, ev, h):
        if ev == 'left':
            self.x -= 1
        elif ev == 'right':
            self.x += 1
        elif ev == 'up':
            self.y -= 1
        elif ev == 'down':
            self.y += 1
        elif ev == 'pageup':
            self.y -= h
        elif ev == 'pagedown':
            self.y += h

        if self.y >= len(self.l):
            self.y = len(self.l) - 1

        if self.y < 0:
            self.y = 0

        if self.x > len(self.l[self.y]):
            self.x = len(self.l[self.y])

        if self.x < 0:
            self.x = 0

    def handle_char(self, ch):
        pass


class EditorWidget:
    def __init__(self, w, h, d):
        self.e = Editor(d)

        self.x = 0
        self.y = 0
        self.w = w
        self.h = h

    def pixels(self):
        bx = self.x
        by = self.y

        ex = bx + self.w
        ey = by + self.h

        bc = black()
        wc = white()

        for x, y, c in self.e.render(bx, by, ex, ey):
            yield x - bx, y - by, Point(c, bc, wc)

        yield self.cx, self.cy, Point(' ', wc, wc)

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

        while self.cx < 0:
            self.x -= self.hw

        while self.cy < 0:
            self.y -= self.hh

        while self.cx >= self.w:
            self.x += self.hw

        while self.cy >= self.h:
            self.y += self.hh


class MessageBar:
    def __init__(self, w):
        self.w = w
        self.t = ''

    def append(self, t):
        self.t += ', ' + str(t)

        if len(self.t) > self.w:
            self.t = self.t[-self.w:]

    def pixels(self):
        b = black()
        w = white()

        for x, ch in enumerate(self.t):
            yield x, 0, Point(ch, b, w)

    def dispatch(self, ev):
        pass


@contextlib.contextmanager
def channel():
    ch = Channel()

    try:
        yield ch
    finally:
        ch.fini()


def main():
    with channel() as ch:
        c = Composer(ch)

        c.add_widget(Panel(c.d.dx, c.d.dy, black()))
        c.i.set_cb(c.add_widget(MessageBar(c.d.dx)).move(0, c.d.dy - 1).w.append)
        c.add_widget(EditorWidget(c.d.dx, c.d.dy - 1, open(sys.argv[1]).read()))

        c.loop()


try:
    main()
    #cProfile.run('main()')
except KeyboardInterrupt:
    pass
