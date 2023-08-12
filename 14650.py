n = int(input())

dp=[[0 for _ in range(n+1)] for _ in range(3)]
if n == 1:
    print(0)
else:
    dp[1][2]=1
    dp[2][2] = 1

    for j in range(3,n+1):
        for i in range(3):
            if i ==0:
                dp[i][j] = dp[i+1][j-1] + dp[i+2][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]


    ans = 0
    for i in range(3):
        ans += dp[i][-1]
    print(ans)