n = int(input())
l = [0]+list(map(int,input().split()))

dp=[0]*(n+1)

for i in range(1,n+1):
    for j in range(i):
        if l[i]>l[j]:
            dp[i] = max(dp[i],dp[j]+1)
        print(dp)
print(max(dp))