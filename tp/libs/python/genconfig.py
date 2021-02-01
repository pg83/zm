import os

win = set(['nt', '_overlapped', '_winapi', 'msvcrt', 'winreg', 'winsound'])
unix = set([])
linux = set(['spwd'])
darwin = set(['_scproxy'])
disabled = set(['_ctypes', '_locale', 'readline', '_curses', '_curses_panel', '_dbm', '_gdbm', '_sqlite3', '_tkinter', '_uuid', 'nis', 'ossaudiodev'])

modules = set(['posix'])

for a, b, c in os.walk('.'):
    for x in c:
        p = os.path.join(a, x)

        if '.c' not in p:
            continue

        if 'test' in p:
            continue

        with open(p, 'r') as f:
            try:
                data = f.read()
            except Exception:
                data = ''

        for l in data.split('\n'):
            if 'PyInit_' not in l:
                continue

            if '"' in l:
                continue

            if '#' in l:
                continue

            if '//' in l:
                continue

            if '/*' in l:
                continue

            if '*/' in l:
                continue

            p = l.find('PyInit_')
            l = l[p + 7:].split('(')[0]

            modules.add(l)


p1 = ''
p2 = ''


def fmt(m, d):
    if m in disabled:
        return '// ' + d

    if m in win:
        return '#if defined(_MSC_VER)\n' + d + '\n#endif'

    if m in unix:
        return '#if !defined(_MSC_VER)\n' + d + '\n#endif'

    if m in darwin:
        return '#if defined(__APPLE__)\n' + d + '\n#endif'

    if m in linux:
        return '#if defined(__linux__)\n' + d + '\n#endif'

    return d


def fmt_p1(m):
    return fmt(m, 'extern PyObject* PyInit_' + m + '();')


def fmt_p2(m):
    return fmt(m, '    {"' + m + '", PyInit_' + m + '},')


for m in sorted(modules):
    p1 += fmt_p1(m) + '\n'
    p2 += fmt_p2(m) + '\n'


extra1 = """
extern PyObject* PyMarshal_Init(void);
extern PyObject* _PyWarnings_Init(void);
"""


extra2 = """
    {"marshal", PyMarshal_Init},
    {"_warnings", _PyWarnings_Init},
    {"builtins", NULL},
    {"sys", NULL},
    {0, 0}
"""

data = '#include "Python.h"\n\n\n'
data += p1
data += extra1
data += '\n\n'
data += 'struct _inittab _PyImport_Inittab[] = {\n'
data += p2
data += extra2
data += '\n};'

data = data.replace('\n\n', '\n')

print(data)
