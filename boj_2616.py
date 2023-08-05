n = int(input())
l = list(map(int,input().split()))
m = int(input())

if m == n/3:
    1/0

prel = [0]
for _ in range(n):
    prel.append(prel[-1]+l[_])
dp=[[0 for _ in range(n+1)]for _ in range(4)]

for i in range(1,4):
    for j in range(m,n+1):
        dp[i][j] = max(dp[i][j-1],dp[i-1][j-m] +prel[j]-prel[j-m])

print(dp[-1][-1])