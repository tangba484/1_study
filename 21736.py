from collections import deque
n,m = map(int,input().split())

g=[list(input())for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if g[i][j] == "I":
            q = deque([[i,j]])
            visited[i][j] = 1
dx,dy = [-1,1,0,0],[0,0,-1,1]
def bfs():
    cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            X,Y = x+dx[i],y+dy[i]
            if 0<=X<n and 0<=Y<m:
                if not visited[X][Y] and g[X][Y] != "X":
                    visited[X][Y] = 1
                    if g[X][Y] == "P":
                        cnt +=1
                    q.append([X,Y])
    return cnt
ans = bfs()
if ans == 0:
    print("TT")
else:
    print(ans)
