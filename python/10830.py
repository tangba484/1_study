n,b = map(int,input().split())

a =[]
for _ in range(n):
    a.append(list(map(int,input().split())))
def mul(X,Y):
    m =[[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                m[i][j] += X[i][k]*Y[k][j]
                m[i][j] %= 1000
    return m
I = [[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    I[i][i] = 1

def R(k):
    if k == 1:
        return mul(a,I)
    elif k == 2:
        return mul(a,a)

    r = R(k//2)
    if k%2 == 1:
        return mul(mul(r,r),a)
    else:
        return mul(r,r)
ans = R(b)

for i in ans:
    print(*i)