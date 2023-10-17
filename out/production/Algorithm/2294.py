n,k = map(int,input().split())
coins=[]
for _ in range(n):
    coins.append(int(input()))
coins.sort()

dp =[100000]*(k+1)
dp[0] = 0
for i in range(1,k+1):
    
    for j in range(n):
        c = coins[j]
        if i>=c:
            if i == c:
                dp[i] = 1
            else:
                if i-c>=0:
                    dp[i] = min(dp[c] + dp[i-c],dp[i])
if dp[-1] == 100000:
    print(-1)
else:
    print(dp[-1])