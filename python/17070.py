n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))


stack = [[0,1,0]]

def dfs():
    cnt = 0
    while stack:
        x,y,state = stack.pop()
        if x==n-1 and y == n-1:
            cnt +=1
            continue
        if state==0:
            if 0<=x<n and y+1<n:
                if graph[x][y+1] ==0:
                    stack.append([x,y+1,0])
            if x+1<n and y+1<n:
                if graph[x][y+1]==0 and graph[x+1][y]==0 and graph[x+1][y+1] ==0:
                    stack.append([x+1,y+1,2])
        if state == 1:
            if x+1<n and y<n:
                if graph[x+1][y] == 0:
                    stack.append([x+1,y,1])
            if x+1<n and y+1<n:
                if graph[x][y+1]==0 and graph[x+1][y]==0 and graph[x+1][y+1] ==0:
                    stack.append([x+1,y+1,2])
        if state==2:
            if 0<=x<n and y+1<n:
                if graph[x][y+1] ==0:
                    stack.append([x,y+1,0])          
            if x+1<n and y<n:
                if graph[x+1][y] == 0:
                    stack.append([x+1,y,1])
            if x+1<n and y+1<n:
                if graph[x][y+1]==0 and graph[x+1][y]==0 and graph[x+1][y+1] ==0:
                    stack.append([x+1,y+1,2])
    return cnt
print(dfs())