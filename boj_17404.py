n = int(input())

G = []
for _ in range(n):
    G.append(list(map(int,input().split())))
ans = float("inf")
for x in (0,1,2):
    dp=[[float("inf") for _ in range(3)]for _ in range(n+1)]
    dp[1][x] = G[0][x]
    for i in range(2,n+1):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + G[i-1][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + G[i-1][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + G[i-1][2]
    dp[n][x] = float('inf')
    ans = min(ans , min(dp[n]))
print(ans)