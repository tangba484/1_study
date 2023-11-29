n = int(input())
l = list(map(int,input().split()))

dp = [0]*(n+1)
ans = 0
for i in range(n):
    x = l[i]
    dp[x] = dp[x-1] + 1
    ans = max(dp[x],ans)

print(n-ans)
