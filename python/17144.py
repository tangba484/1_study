n,m,t = map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j] == -1:
            up = [i-1,j]
            do = [i,j]
            break

dx,dy = [-1,1,0,0],[0,0,-1,1]
def china():
    a=[[-1 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] >=0:
                a[i][j] = graph[i][j]//5
    
    for i in range(n):
        for j in range(m):
            cnt = 0
            S = 0
            if a[i][j] >=0:
                for k in range(4):
                    DX,DY = i+dx[k],j+dy[k]
                    if 0<=DX<n and 0<=DY<m:
                        if a[DX][DY] >=0:
                            S += a[DX][DY]
                            cnt += 1
            graph[i][j] = graph[i][j] -a[i][j]*cnt + S
    return graph
def wind(up,do,graph):
    x = up[0]
    for i in range(x-1,0,-1):
        graph[i][0] = graph[i-1][0]
    for i in range(0,m-1):
        graph[0][i] = graph[0][i+1]
    for i in range(0,x):
        graph[i][-1] = graph[i+1][-1]
    graph[x] = [-1]+[0]+graph[x][1:m-1]

    x = do[0]
    for i in range(x+1,n-1):
        graph[i][0] = graph[i+1][0]
    for i in range(m-1):
        graph[-1][i] = graph[-1][i+1]
    for i in range(n-1,x,-1):
        graph[i][-1] = graph[i-1][-1]
    graph[x] = [-1]+[0]+graph[x][1:m-1]

    return graph

for _ in range(t):
    graph = china()
    graph = wind(up,do,graph)

ans = 0
for i in graph:
    ans += sum(i)
print(ans+2)