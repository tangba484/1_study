from itertools import combinations as cb
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
dx,dy = [-1,1,0,0],[0,0,-1,1]
can = []
virus=[]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            can.append([i,j])
        elif graph[i][j] == 2:
            virus.append([i,j])


def infection(a,b,c,G,Vir):
    visited =[[0 for _ in range(m)] for _ in range(n)]
    G[a[0]][a[1]] = 1
    G[b[0]][b[1]] = 1
    G[c[0]][c[1]] = 1
    q = Vir
    while q:
        x,y = q.pop()
        visited[x][y] = 1
        for i in range(4):
            DX,DY = x+dx[i],y+dy[i]
            if 0<=DX<n and 0<=DY<m:
                if not visited[DX][DY] and G[DX][DY] == 0:
                    visited[DX][DY] = 1
                    G[DX][DY] = 9
                    q.append([DX,DY])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if G[i][j] == 0:
                cnt += 1
    return cnt
CB = cb(can,3)
ans = 0
for a,b,c in CB:
    G = [i[:] for i in graph]
    Vir = virus[:]
    ans = max(ans,infection(a,b,c,G,Vir))
print(ans)
