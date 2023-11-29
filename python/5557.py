n = int(input())

l = [0]+list(map(int,input().split()))
target = l[-1]
# dp[i][j] i번째 수를 다룰째 j값이 나오는 경우
dp = [[-1 for _ in range(21)]for _ in range(n)]
dp[1][l[1]] = 1
for i in range(2,n):
    
    for j in range(21):
        if dp[i-1][j] >=0:
            if 0<=j + l[i] <= 20:
                if dp[i][j+l[i]] == -1:
                    dp[i][j+l[i]] = 0
                    dp[i][j+l[i]] = dp[i-1][j]
                else:
                    dp[i][j+l[i]] += dp[i-1][j]
            if 0<= j - l[i] <= 20:
                if dp[i][j - l[i]] == -1 :
                    dp[i][j - l[i]] = 0
                    dp[i][j - l[i]] = dp[i-1][j]
                else:   
                    dp[i][j - l[i]] += dp[i-1][j]

if dp[-1][target] == -1:
    print(0)
else:
    print(dp[-1][target])