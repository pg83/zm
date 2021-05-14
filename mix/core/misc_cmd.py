import os
import sys

import core.shell as cs
import core.shell_cmd as csc


class Iface:
    def untar(self, path):
        csc.untar(path)

    def fetch_url(self, url, out):
        csc.fetch_url(url, out)


def cli_misc_runpy(ctx):
    sys.argv = ['runpy'] + ctx['args']

    g = {
        'mix': Iface(),
    }

    exec(sys.stdin.read(), g, g)


def cli_misc_runpsh(ctx):
    def iter_env():
        yield from os.environ.items()

        for k, v in enumerate(['runpsh'] + ctx['args']):
            yield str(k), v

    cs.interpret(sys.stdin.read(), dict(iter_env()))


def cli_misc_untar(ctx):
    for a in ctx['args']:
        csc.untar(a)
