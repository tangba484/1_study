N = int(input())

dp = [[0 for _ in range(10)]for _ in range(N+1)]

for i in dp:
    i[0] = 1
    
for i in range(1,N+1):
    for j in range(1,10):
        dp[i][j] = (dp[i][j-1]%10007 + dp[i-1][j]%10007)%10007

print(sum(dp[-1])%10007)