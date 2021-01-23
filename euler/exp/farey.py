def farey_sequence(n):
    (a, b, c, d) = (0, 1, 1, n)

    yield a, b

    while c <= n:
        k = (n + b) // d

        (a, b, c, d) = (c, d, k * c - a, k * d - b)

        yield a, b

for a, b in farey_sequence(8):
    print(a, '/', b)
