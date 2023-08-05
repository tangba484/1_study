n = int(input())
dp =[[0]*n for _ in range(3)]
for i in range(3):
    dp[i][0] = 1



for j in range(1,n):
    for i in range(3):
        if i ==0:
            dp[i][j] = (dp[i][j-1]%9901 + dp[i+1][j-1]%9901+ dp[i+2][j-1]%9901)%9901
        elif i == 1:
            dp[i][j] = (dp[i-1][j-1]%9901 + dp[i+1][j-1]%9901)%9901
        else:
            dp[i][j] = (dp[i-1][j-1]%9901 + dp[i-2][j-1]%9901)%9901
ans = 0
for i in dp:
    ans += i[-1]%9901
print(ans%9901)