n = int(input())
dp = [0 for _ in range(n+1)]
if n%2 == 1:
    print(0)
else:
    dp[0],dp[2] = 1,3


    for i in range(3,n+1):
        if i % 2 == 1:
            continue
        else:
            dp[i] = dp[i-2]*3
            for j in range(0,i-2,2):
                dp[i] += dp[j]*2
    print(dp[-1])