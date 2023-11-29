N,M = map(int,input().split())
r,c,d = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

ans=0

while 1:
    if d ==0:
        b1,b2=r+1,c
    elif d == 1:
        b1,b2 = r,c-1
    elif d ==2:
        b1,b2 = r-1,c
    else:
        b1,b2 = r,c+1
    if graph[r][c] == 0:
        graph[r][c] = 2
        ans += 1
    if graph[r+1][c] !=0 and graph[r-1][c]!=0 and graph[r][c-1] !=0 and graph[r][c+1] != 0:
        if graph[b1][b2] != 1:
            r,c = b1,b2
            continue
        elif graph[b1][b2] == 1:
            break
    if graph[r+1][c] ==0 or graph[r-1][c] ==0 or graph[r][c-1] ==0 or graph[r][c+1] == 0:
        d = (d+3)%4
        if d ==0:
            f1,f2 = r-1,c
        elif d == 1:
            f1,f2 = r,c+1
        elif d ==2:
            f1,f2 = r+1,c
        else:
            f1,f2 = r,c-1
        if graph[f1][f2] == 0:
            r,c = f1,f2
            continue
print(ans)    