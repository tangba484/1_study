n = int(input())
l = list(map(int,input().split()))

dp = [1]*(n)
dp[0] = 1
for i in range(1,n):
    for j in range(i):
        if l[i]>l[j]:
            dp[i] = max(dp[i],dp[j] + 1)

dp_ = [1]*n

l = l[::-1]
for i in range(1,n):
    for j in range(i):
        if l[i]>l[j]:
            dp_[i] = max(dp_[i],dp_[j] + 1)

dp_ = dp_[::-1]
ans = 0
for i in range(n):
    ans = max(ans,dp[i]+dp_[i]-1)
print(ans)
        