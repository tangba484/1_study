n,m = map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
dx,dy = [-1,1,0,0],[0,0,-1,1]
for i in range(m):
    graph[0][i] =-1
    graph[n-1][i] = -1
for i in range(n):
    graph[i][0] = -1
    graph[i][m-1] = -1

def check():
    stack = [[0,0]]
    visited=[[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    while stack:
        x,y = stack.pop()
        for i in range(4):
            DX,DY = x+dx[i],y+dy[i]
            if 0<=DX < n and 0<= DY <m:
                if graph[DX][DY] != 1 and not visited[DX][DY]:
                    if graph[DX][DY] == 0:
                        graph[DX][DY] = -1
                    visited[DX][DY] = 1
                    stack.append([DX,DY])
def R():
    box=[]
    for x in range(1,n-1):
        for y in range(1,m-1):
            if graph[x][y] == 1:
                cnt = 0
                for t in range(4):
                    DX,DY = x+dx[t] , y+dy[t]
                    if 0<=DX < n and 0<= DY <m:
                        if graph[DX][DY] == -1:
                            cnt += 1
                if cnt >= 2:
                    box.append([x,y])
    for x,y in box:
        graph[x][y] = -1
    if box:
        return 1
    else:
        return 0
k = 1
C = 0
check()
while k!=0:
    C += 1
    check()
    k = R()
print(C-1)