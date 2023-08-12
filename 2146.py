from collections import deque
n = int(input())

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

visited = [[0 for _ in range(n)] for _ in range(n)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
map =[]
def find():
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                q = deque([[i,j]])
                vst=[[i,j]]
                while q:
                    x,y, = q.popleft()
                    for t in range(4):
                        X,Y = x+dx[t],y+dy[t]
                        if 0<=X<n and 0<=Y<n:
                            if not visited[X][Y] and g[X][Y] == 1:
                                vst.append([X,Y])
                                q.append([X,Y])
                                visited[X][Y] = 1
                if vst:
                    map.append(vst)
find()
result = []

def bfs(M):
    G = [i[:] for i in g]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = deque([])
    for x,y in M:
        visited[x][y] = 1
        q.append([x,y,0])
    
    while q:
        x,y,c = q.popleft()

        for i in range(4):
            X,Y = x+dx[i],y+dy[i]
            if 0<=X<n and 0<=Y<n:
                if G[X][Y] == 1 and not visited[X][Y]:
                    return c
                if not visited[X][Y] and G[X][Y] ==0:
                    G[X][Y] = 9
                    visited[X][Y] = 1
                    q.append([X,Y,c+1])
for M in map:
    result.append(bfs(M))
print(min(result))
