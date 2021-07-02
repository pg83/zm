import sys
import importlib


CLIS = [
    ('core.build', 'build'),
    ('core.cache', 'cache'),
    ('core.sh', 'sh'),
    ('core.misc_cmd', 'misc_runpy'),
    ('core.misc_cmd', 'misc_runph'),
    ('core.misc_cmd', 'misc_untar'),
    ('core.misc_cmd', 'misc_unzip'),
]


def find_handler(args):
    sent = '$$'
    xargs = sent.join(args)

    for k, v in CLIS:
        vv = v.replace('_', sent)

        if xargs.startswith(vv):
            a = xargs[len(vv):].split(sent)

            while a and a[0] == '':
                a = a[1:]

            return k, v, a


def print_help():
    print('usage: mix <command>:')

    for k, v in CLIS:
        print('    ' + v.replace('_', ' '))


def main(args, binary):
    hndl = find_handler(args)

    if hndl:
        k, v, a = hndl

        ctx = {
            'args': a,
            'binary': binary,
        }

        importlib.import_module(k).__dict__['cli_' + v](ctx)
    else:
        print_help()
        sys.exit(1)
