res = 0

for a in range(1, 1001):
    print(a ** a)

    res += a ** a

print(str(res)[-10:])
