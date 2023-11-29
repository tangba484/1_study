n = int(input())

dp1=[1]
dp2=[1]
iter = 2
s = 1
while True:
    dp1.append(dp1[-1]+iter)
    s = s+ dp1[-1]
    dp2.append(s)
    iter += 1
    if s > n:
        break

dp2.pop()

dp = [99999]*(n+1)
dp[0] = 0
dp[1] = 1

for i in range(1,n+1):
    for num in dp2:
        if i == num:
            dp[i]=1
            break
        elif num > i:
            break
        dp[i] = min(dp[i-1]+1,dp[num]+dp[i-num],dp[i])

print(dp[-1])
