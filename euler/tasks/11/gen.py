import sys

res = ''

for l in sys.stdin:
    res += l.strip().replace(' ', ', ').replace(', 0', ',  ') + ',\n'

print(res.replace('\n0', '\n '))
