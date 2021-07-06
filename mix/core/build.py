import os
import subprocess

import core.build as cb
import core.manager as cm
import core.cmd_line as cc


def execute_cmd(c):
    if 'func' in c:
        return c['func']()

    try:
        subprocess.run(c['args'], input=c.get('stdin', '').encode(), env=c.get('env', {}), check=True)
    except Exception as e:
        raise Exception(f'while build {c}: {e}')


def iter_in(c):
    if 'in' in c:
        yield from c['in']

    if 'in_dir' in c:
        for x in c['in_dir']:
            yield x + '/touch'


def iter_out(c):
    if 'out' in c:
        yield from c['out']

    if 'out_dir' in c:
        for x in c['out_dir']:
            yield x + '/touch'


def touch_func(p):
    def func():
        with open(p, 'w') as f:
            pass

    return func


def iter_cmd(c):
    if 'cmd' in c:
        yield from c['cmd']

    if 'out_dir' in c:
        for x in c['out_dir']:
            yield {
                'func': touch_func(x + '/touch'),
            }


def execute_node(n):
    for o in iter_out(n):
        if os.path.exists(o):
            print(o + ' complete')
        else:
            for c in iter_cmd(n):
                execute_cmd(c)

            return


def execute(g):
    by_out = {}

    for n in g['nodes']:
        for o in iter_out(n):
            by_out[o] = n

    v = set()

    def visit(n):
        if n not in v:
            v.add(n)

            t = by_out[n]

            for x in iter_in(t):
                visit(x)

            execute_node(t)

    for t in g['targets']:
        visit(t)


def cli_build(ctx):
    binary, where, pkgs = cc.parse_pkgs(ctx)

    cb.execute(cm.Manager(binary, where).build_graph(pkgs))
