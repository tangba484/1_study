a,b = map(int,input().split())


def r(n):
    if n == 0:
        return 0
    k = 0
    while 2**k <= n:
        k += 1
    c = k-1
    if 2**c == n:
        return int(c*(2**(c-1))) + 1

    return r(n - 2**c) + int(c*(2**(c-1))) + 1 + n - int(2**c)
print(r(b) -r(a-1))