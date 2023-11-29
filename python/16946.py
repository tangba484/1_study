from collections import deque,defaultdict
n,m = map(int,input().split())
D = defaultdict(int)

graph=[]
for _ in range(n):
    graph.append(input())
dx,dy = [-1,1,0,0],[0,0,-1,1]
A = [[[0] for _ in range(m)]for _ in range(n)]
visited=[[0 for _ in range(m)] for _ in range(n)]
idx = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == "0" and A[i][j][0] == 0 and not visited[i][j]:
            A[i][j][0] = idx
            visited[i][j] = 1
            stack = [[i,j]]
            c = 1
            while stack:
                x,y = stack.pop()
                for k in range(4):
                    DX,DY = x+dx[k],y+dy[k]
                    if 0<=DX<n and 0<=DY<m:
                        if not visited[DX][DY] and graph[DX][DY] == "0":
                            A[DX][DY][0] = idx
                            visited[DX][DY] = 1
                            c += 1
                            stack.append([DX,DY])
            D[idx] = c
            idx += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == "1":
            box = set()
            for k in range(4):
                DX,DY = i+dx[k],j+dy[k]
                if 0<=DX<n and 0<=DY<m:
                    box.add(A[DX][DY][0])
            s=1
            for x in box:
                s += D[x]
            print(s%10,end="")
        else:
            print(0,end="")
    print()