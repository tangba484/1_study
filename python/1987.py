r,c = map(int,input().split())
graph=[]
for _ in range(r):
    graph.append(list(input()))

visited=[0]*(ord("Z")+1)
dx,dy = [-1,1,0,0],[0,0,-1,1]
visited[ord(graph[0][0])] = 1
ans = 1
def R(x,y,cnt):
    global ans
    if cnt>ans:
        ans = cnt
    if ans == 26:
        return 26
    for i in range(4):
        DX,DY = x + dx[i] , y + dy[i]
        if 0<= DX< r and 0<= DY <c:
            if visited[ord(graph[DX][DY])] == 0:
                visited[ord(graph[DX][DY])] = 1
                R(DX,DY,cnt + 1)
                visited[ord(graph[DX][DY])] = 0
R(0,0,1)
print(ans)