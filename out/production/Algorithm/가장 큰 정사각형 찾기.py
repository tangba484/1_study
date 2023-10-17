def solution(B):
    row = len(B)
    col = len(B[0])
    dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
    
    ans=0
    for i in range(1,row+1):
        for j in range(1,col+1):
            if B[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) +1
            
                if dp[i][j] > ans:
                    ans = dp[i][j]
    return ans**2