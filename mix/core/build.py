import os
import subprocess

import core.build as cb
import core.manager as cm


def execute_cmd(c):
    a = c['args']
    p = subprocess.Popen(a, stdin=subprocess.PIPE, env=c.get('env', {}))

    p.communicate(input=c.get('stdin', '').encode('utf-8'))

    if p.wait():
        raise Exception(' '.join(a) + ' failed')


def execute_node(n):
    for c in n['cmd']:
        execute_cmd(c)


def execute(g):
    by_out = {}

    for n in g['nodes']:
        for o in n['out']:
            by_out[o] = n

    v = set()

    def visit(n):
        if n not in v:
            v.add(n)

            t = by_out[n]

            for x in t.get('in', []):
                visit(x)

            execute_node(t)

    for t in g['targets']:
        visit(t)


def cli_build(ctx):
    args = ctx['args']
    binary = ctx['binary']
    where = os.path.join(os.path.dirname(binary), 'pkgs')

    cb.execute(cm.Manager(binary, where).build_graph(args))
