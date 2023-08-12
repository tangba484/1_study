n = int(input())
M = 1000000007

a =[[1,1],[1,0]]

def R(a,n):
    if n == 1:
        return a
    elif n == 2:
        return mul(a,a)
    ans = R(a,n//2)
    if n%2 == 0:
        return mul(ans,ans)
    else:
        return mul(mul(ans,ans),a)

def mul(a,b):
    x=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                x[i][j] += ((a[i][k]%M)*(b[k][j]%M))%M
            x[i][j] %= M
    return x

print(R(a,n)[0][1])