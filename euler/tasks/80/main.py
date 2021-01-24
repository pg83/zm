q = 10 ** 200

def sqrt(x):
    a = 0
    b = x

    while b - a > 1:
        c = (a + b) / 2

        if x < c * c:
            b = c
        else:
            a = c

    return a

ss = set([x * x for x in range(0, 1000)])

def xxx():
    for i in range(1, 100):
        if i not in ss:
            for ch in str(sqrt(i * q))[:100]:
                yield int(ch)

print sum(xxx(), 0)
