def iter_fib():
    a = 1
    b = 1

    while True:
        yield a

        a, b = b, a + b

cnt = 0

for f in iter_fib():
    cnt += 1

    if len(str(f)) >= 1000:
        break

print(cnt)
