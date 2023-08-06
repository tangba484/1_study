n , m = map(int ,input().split())
A = list(map(int, input().split()))
c = list(map(int, input().split()))
S = sum(c)
dp=[[0 for _ in range(S+1)] for _ in range(n+1)]
ans = float("inf")

for i in range(n):
    memory = A[i]
    cost = c[i]
    for j in range(1,S+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-cost]+memory,dp[i-1][j])
        if dp[i][j]>=m:
            ans = min(ans,j)
if m ==0:
    print(0)
else:
    print(ans)