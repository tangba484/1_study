n,s,m = map(int,input().split())

l = list(map(int,input().split()))

DP = [[s]]
for i in range(n):
    dp = DP[-1]
    a = set()
    k = l[i]
    for j in dp:
        if 0<= k + j <=m:
            a.add(k+j)
        if  0<=j-k <=m:
            a.add(j-k)
    DP.append(list(a))
try:
    print(max(DP[-1]))
except:
    print(-1)