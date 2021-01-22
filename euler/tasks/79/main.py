import sys
import collections

deps = collections.defaultdict(list)

with open(sys.argv[1], 'r') as f:
    for l in f:
        l = l.strip()

        if l:
            deps[l[0]].append(l[1])
            deps[l[1]].append(l[2])

v = set()

def visit(n):
    for d in deps.get(n, []):
        yield from visit(d)

    if n not in v:
        v.add(n)

        yield n

print(''.join([str(x) for x in reversed(list(visit('7')))]))
