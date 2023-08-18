import sys
sys.setrecursionlimit(100000)
n = list(input())
k = len(n)
for i in range(k):
    n[i] = int(n[i])

m = 100000000
M = -1
def li(a):
    s = list(str(a[0]))
    ans = []
    for i in s:
        ans += [int(i)]
    return ans
def check(a):
    cnt = 0
    for i in a:
        if i%2 == 1 :
            cnt += 1
    return cnt
def s(a):
    i = 1
    ans=0
    for x in a[::-1]:
        ans += x*i
        i *= 10
    return ans
k =check(n)
def R(a):
    global k,M,m
    print(a,"k = ",k)
    l = len(a)
    if l >= 3:
        for i in range(l-2):
            for j in range(i+1,l-1):
                A = [s(a[:i+1]) + s(a[i+1:j+1]) + s(a[j+1:])]
                k += check(li(A))
                R(li(A))
                k -= check(li(A))
    elif l == 2:
        A = [a[0]+a[1]]
        k += check(li(A))
        R(li(A))
        k -= check(li(A))
    elif l == 1:
        if k > M:
            M = k
        if k < m:
            m = k
        return
R(n)
print(m,M)