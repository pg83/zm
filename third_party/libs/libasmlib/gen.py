import os, sys


def repl(x):
    p = x.find('?OVR_')

    if p < 0:
        return x

    p1 = x.find(':', p)

    if p1 < 0:
        p2 = x.find(';')

        if p2 >= 0 and p2 < p:
            return x

        raise Exception('shit happen ' + x)

    return x[:p] + 'EXP(' + x[p + 5:p1] + ')' + x[p1:]


def repl1(x):
    if 'define ALLOW_OVERRIDE' in x:
        return ''

    return x


for l in os.listdir('.'):
    if l.endswith('.asm'):
        if 'defs.asm' in l:
            continue

        with open(l, 'r') as f:
            data = f.read()

            if not 'defs.asm' in data:
                data = '%include "defs.asm"\n\n' + '\n'.join([repl(x) for x in data.split('\n')])

            if 'ALLOW_OVERRIDE' in data:
                data = '\n'.join([repl1(x) for x in data.split('\n')])

        if 1:
            with open(l, 'w') as f:
                f.write(data)
        else:
            print data
