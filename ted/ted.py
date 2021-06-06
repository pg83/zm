import io
import os
import sys
import tty
import time
import enum
import atexit
import cProfile

from collections import deque
from dataclasses import dataclass


def reset():
    os.system('reset')


def esc(*args):
    return '\033[' + ';'.join(str(x) for x in args)


def move(x, y):
    return esc(y + 1, x + 1) + 'H'


def hide_cursor():
    return esc('?25l')


class Channel:
    def __init__(self):
        self.b = deque()
        self.i = io.FileIO(0, 'r')
        self.o = io.FileIO(1, 'w')

        tty.setraw(self.i)

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
        self.send(move(10000, 10000) + esc('6n'))

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

    def next(self):
        key = self.ch.next()

        if key == 27:
            return self.scan_escape()

        if key == 3:
            return 'ctrlc'

        return chr(key)

    def scan_escape(self):
        p = ''

        while True:
            p += chr(self.ch.next())

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
        return esc(48, 2, self.r, self.g, self.b) + 'm'

    def fg(self):
        return esc(38, 2, self.r, self.g, self.b) + 'm'


@dataclass
class Color8:
    n: int

    def bg(self):
        return esc(48, 5, self.n) + 'm'

    def fg(self):
        return esc(38, 5, self.n) + 'm'


def bg4(n):
    if n < 8:
        return esc(40 + n) + 'm'

    return esc(92 + n) + 'm'


def fg4(n):
    if n < 8:
        return esc(30 + n) + 'm'

    return esc(82 + n) + 'm'


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
        self.ch.send(hide_cursor())
        self.d = ['' for i in range(dx * dy)]

    def flip(self, pixels):
        d = ''
        byp = {}

        for x, y, n in pixels:
            if x >= 0 and x < self.dx and y >= 0 and y < self.dy:
                byp[x + y * self.dx] = (x, y, n)

        for p, (x, y, n) in byp.items():
            f = n.fmt()

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

            if c in ('ctrlc', 3, chr(3)):
                raise KeyboardInterrupt()

            self.s[self.o[-1]].dispatch(c)

            def pixels():
                for o in self.o:
                    yield from self.s[o].pixels()

            self.d.flip(pixels())


class SimpleInput:
    def __init__(self, w):
        self.w = w
        self.t = ''

    def dispatch(self, ev):
        self.t += ev

    def pixels(self):
        x = 0
        y = 0

        for i in range(0, len(self.t)):
            yield x, y, Point(self.t[i], black(), white())

            x += 1

            if x >= self.w:
                x = 0
                y += 1


class Editor:
    def __init__(self, d):
        self.l = d.split('\n')

    def render(self):
        for y, l in enumerate(self.l):
            for x, c in enumerate(l):
                yield x, y, c


class EditorWidget:
    def __init__(self, w, h, d):
        self.e = Editor(d)

        self.x = 0
        self.y = 0
        self.w = w
        self.h = h

        self.cx = 0
        self.cy = 0

    def pixels(self):
        bx = self.x
        by = self.y

        ex = bx + self.w
        ey = by + self.h

        bc = black()
        wc = white()

        for x, y, c in self.e.render():
            if x >= bx and x < ex and y >= by and y < ey:
                yield x - bx, y - by, Point(c, bc, wc)

        yield self.cx, self.cy, Point(' ', wc, wc)

    @property
    def hw(self):
        return self.w // 2

    @property
    def hh(self):
        return self.h // 2

    def dispatch(self, ev):
        if ev == 'left':
            self.cx -= 1
        elif ev == 'right':
            self.cx += 1
        elif ev == 'up':
            self.cy -= 1
        elif ev == 'down':
            self.cy += 1
        elif ev == 'pageup':
            self.y -= self.h
        elif ev == 'pagedown':
            self.y += self.h

        if self.cx < 0:
            self.cx += self.hw
            self.x -= self.hw

        if self.x < 0:
            self.x = 0
            self.cx = 0

        if self.cy < 0:
            self.cy += self.hh
            self.y -= self.hh

        if self.y < 0:
            self.y = 0
            self.cy = 0

        if self.cx >= self.w:
            self.cx -= self.hw
            self.x += self.hw

        if self.cy >= self.h:
            self.cy -= self.hh
            self.y += self.hh


def main():
    c = Composer(Channel())

    c.add_widget(Panel(c.d.dx, c.d.dy, black()))
    c.add_widget(EditorWidget(c.d.dx, c.d.dy, open(sys.argv[1]).read()))

    c.loop()


try:
    def run():
        try:
            main()
        finally:
            reset()

    run()
    #cProfile.run('run()')
except KeyboardInterrupt:
    pass
