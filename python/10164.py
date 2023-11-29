n,m,k = map(int,input().split())
graph = [[(j-1)*m + i for i in range(m+1)] for j in range(n+1)]
for i in range(n+1):
    graph[i][0]=0
for i in range(m+1):
    graph[0][i] = 0
dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
dp[1][1] = 1
if k ==0:
    for i in range(m+1):
        dp[1][i] = 1
    for i in range(n+1):
        dp[i][1] = 1
    for i in range(2,n+1):
        for j in range(2,m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[-1][-1])
else:
    for i in range(n+1):
        for j in range(m+1):
            if graph[i][j] == k:
                x,y = i,j

    for i in range(y+1):
        dp[1][i] = 1
    for i in range(x+1):
        dp[i][1] = 1
    for i in range(2,x+1):
        for j in range(2,y+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    a = dp[x][y]
    for i in range(x,n+1):
        dp[i][y] = 1
    for j in range(y,m+1):
        dp[x][j] = 1

    for i in range(x+1,n+1):
        for j in range(y+1,m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(a*dp[-1][-1])