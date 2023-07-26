X = 1000000007
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
def f(x,y,a,b):
    q = a*x + b*y
    p = a*y
    g = gcd(q,p)
    return int(q/g),int(p/g)
def R(a,n):
    if n == 1:
        return a
    elif n == 2:
        return a*a
    ans = R(a,n//2)
    if n%2==0:
        return ((ans%X)*(ans%X))%X
    else:
        return ((ans%X)*(ans%X)*a)%X

m = int(input())
b,a = 0,1
ans = 0
for _ in range(m):
    x,y = map(int,input().split())
    p,q = f(x,y,a,b)
    ans += R(p,X-2)*q
    ans %= X
print(ans)