import os
import sys
import shutil

import core.shell as cs
import core.shell_cmd as csc


def prepare_dir(d):
    try:
        shutil.rmtree(d)
    except FileNotFoundError:
        pass

    os.makedirs(d)


class Iface:
    def untar(self, path):
        csc.untar(path)

    def unzip(self, path):
        csc.unzip(path)

    def fetch_url(self, url, out):
        csc.fetch_url(url, out)

    def header(self):
        out = os.environ['out']
        tmp = os.environ['tmp']

        prepare_dir(out)
        prepare_dir(tmp)

        os.chdir(tmp)

    def footer(self):
        out = os.environ['out']
        tmp = os.environ['tmp']

        shutil.rmtree(tmp)

        with open(out + '/touch', 'w') as f:
            pass


def cli_misc_runpy(ctx):
    sys.argv = ['runpy'] + ctx['args']

    g = {
        'mix': Iface(),
    }

    exec(sys.stdin.read(), g, g)


def cli_misc_runph(ctx):
    def iter_env():
        yield from os.environ.items()

        for k, v in enumerate(['runph'] + ctx['args']):
            yield str(k), v

    cs.interpret(sys.stdin.read(), dict(iter_env()))


def cli_misc_untar(ctx):
    for a in ctx['args']:
        csc.untar(a)


def cli_misc_unzip(ctx):
    for a in ctx['args']:
        csc.unzip(a)
