
m,n = map(int,input().split())
g = []
for _ in range(m):
    g.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
dp =[[-1 for _ in range(n)] for _ in range(m)]
def R(x,y):
    if x == m-1 and y == n-1:
        return 1
    
    if dp[x][y] == -1:
        dp[x][y] = 0

        for i in range(4):
            X,Y = x+dx[i],y+dy[i]

            if 0<= X <m and 0<=Y < n:
                if g[x][y] > g[X][Y]:
                    dp[x][y] += R(X,Y)
    return dp[x][y]
print(R(0,0))