from collections import deque
n,m = map(int,input().split())
g =[list(map(int,input().split())) for _ in range(n)]
visited=[[0 for _ in range(m)]for _ in range(n)]

dx,dy =[-1,1,0,0],[0,0,-1,1]
for i in range(n):
    if 2 in g[i]:
        q = deque([[i,g[i].index(2),0]])
        visited[q[0][0]][q[0][1]] = 1
        break
answer =[[0 for _ in range(m)]for _ in range(n)]
answer[q[0][0]][q[0][1]] = 0
def bfs(q):
    
    while q:
        x,y,c = q.popleft()
        for i in range(4):
            X,Y = x+dx[i],y+dy[i]
            if 0<=X <n and 0<=Y <m :
                if not visited[X][Y] and g[X][Y] == 1:
                    visited[X][Y] = 1
                    answer [X][Y] = c+1
                    q.append([X,Y,c+1])
bfs(q)

for i in range(n):
    for j in range(m):
        if answer[i][j] == 0 and g[i][j] == 1:
            answer[i][j] = -1
for i in answer:
    print(*i)
        