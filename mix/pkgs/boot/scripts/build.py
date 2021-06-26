import os
import subprocess


DATA = r'''
{{mix.files.build_sh.data}}
'''


def iter_lines():
    yield 'set -e'
    yield 'set -x'

    for p in reversed(os.environ['PATH'].split(':')):
        pp = os.path.normpath(os.path.join(p, '..', 'env'))

        if os.path.isfile(pp):
            yield '. ' + pp

    yield DATA


p = subprocess.Popen([mix.which('dash')], stdin=subprocess.PIPE, shell=False)
p.communicate(input=('\n'.join(iter_lines())).encode())

if p.wait():
    raise Exception('shit happen')
