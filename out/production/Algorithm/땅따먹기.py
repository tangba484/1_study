def solution(land):
    dp=[[0]*4 for _ in range(len(land))]
    for i in range(4):
        dp[0][i]=land[0][i]
    for i in range(1,len(land)):
        for k in range(4):
            dp[i][k]=max(dp[i-1][j]+land[i][k] for j in range(4) if j!=k)
    return (max(dp[-1]))