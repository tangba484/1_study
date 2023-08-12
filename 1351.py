n,p,q = map(int,input().split())
d = {}
def R(n):
    if n == 0:
        return 1
    if n in d:
        return d[n]
    x = R(int(n/p))
    y = R(int(n/q))
    d[n] = x+y
    return d[n]
print(R(n))