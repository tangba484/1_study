n = int(input())

dp =[[0 for _ in range(3)] for _ in range(n+2)]

dp[2][0] = 3
dp[2][1] = 1
dp[2][2] = 1

for i in range(4,n+2,2):
    dp[i][0] = dp[i-2][0]*3 + dp[i-2][1]*2
    dp[i][1] = dp[i-2][1] + dp[i-2][0]
    dp[i][2] = dp[i-2][2] + dp[i-2][0]
print(dp[n][0])