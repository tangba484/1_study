t = int(input())
n = int(input())
A = list(map(int,input().split()))

m = int(input())
B = list(map(int,input().split()))
if m > n:
    A,B = B,A
    m,n = n,m
Ap=[A[0]]
for i in range(1,n):
    Ap.append(Ap[-1] + A[i])
Bp = [B[0]]
for i in range(1,m):
    Bp.append(Bp[-1] + B[i])

def sa(i,j):
    if i == 0:
        return Ap[j]

    return Ap[j] -Ap[i-1]

bt = []
for i in range(m):
    for j in range(i+1):
        if j ==0:
            bt.append(Bp[i])
        else:
            bt.append(Bp[i] - Bp[j-1])
bt.sort()
D={}
for i in bt:
    if i not in D:
        D[i] = 1
    else:
        D[i] += 1
k = len(bt)
ans = 0
def sol(target,k):
    global ans
    start = 0
    end = k

    while start + 1 < end:
        mid = (start + end)//2
        if target > bt[mid]:
            start = mid
        else:
            end = mid
    if end == k:
        if bt[start] == target:
            ans += D[target]
    else:
        if bt[start] == target or bt[end] == target:
            ans += D[target]

for i in range(n):
    for j in range(i+1):
        target = t - sa(j,i)
        sol(target,k)
print(ans)