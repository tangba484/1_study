d, k = map(int,input().split())

dp=[0 for _ in range(d+1)]

dp[d] = k
# print(dp)

for i in range(k,-1,-1):
    dp[d-1] = i
    flag = 0
    for j in range(d-2,0,-1):
        dp[j] = dp[j+2] - dp[j+1]
        if dp[j] <= 0 or dp[j]>dp[j+1]:
            flag=1
            break
    if flag==0:
        ans = f"{dp[1]}\n{dp[2]}"
    # print(dp)
print(ans)