import os
import subprocess

import core.build as cb
import core.manager as cm


def execute_cmd(c):
    if 'func' in c:
        return c['func']()

    a = c['args']
    p = subprocess.Popen(a, stdin=subprocess.PIPE, env=c.get('env', {}))

    p.communicate(input=c.get('stdin', '').encode('utf-8'))

    if p.wait():
        raise Exception(' '.join(a) + ' failed')


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
    args = ctx['args']
    binary = ctx['binary']
    where = os.path.join(os.path.dirname(binary), 'pkgs')

    cb.execute(cm.Manager(binary, where).build_graph(args))
