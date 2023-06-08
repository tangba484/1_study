n = int(input())

L = list(map(int,input().split()))
L = [0] + L
dp = [0]*(n+1)
dp[1] = 1

for i in range(2,n+1):
    if L[i] >= dp[i-1] + 1:
        dp[i] = dp[i-1] +1
    else:
        dp[i] = L[i]
print(max(dp))