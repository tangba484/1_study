from collections import deque
def solution(maps):
    graph,result=[],[]
    for i in maps:
        graph.append(list(i))
    rl,cl = len(graph),len(graph[0])
    visited=[[0 for _ in range(cl)]for _ in range(rl)]
    def bfs(q):
        dx,dy=[-1,1,0,0],[0,0,-1,1]
        s=int(graph[q[0][0]][q[0][1]])
        while q:
            x,y = q.popleft()
            for i in range(4):
                DX,DY = x+dx[i],y+dy[i]
                if 0<=DX<rl and 0<= DY <cl :
                    if not visited[DX][DY] and graph[DX][DY] != "X":
                        visited[DX][DY] = 1
                        s += int(graph[DX][DY])
                        q.append([DX,DY])
        return result.append(s)
    for i in range(rl):
        for j in range(cl):
            if graph[i][j] != "X" and not visited[i][j]:
                q = deque([[i,j]])
                visited[i][j] = 1
                bfs(q)
    if len(result) == 0:
        return [-1]
    else:
        return sorted(result)