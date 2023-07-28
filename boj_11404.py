import sys
input=sys.stdin.readline

n = int(input())
m = int(input())
INF = float("inf")
graph=[[INF for _ in range(n+1)]for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b],c)

for k in range(1,n+1):
    graph[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] =min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == float("inf"):
            print(0,end=" ")
        else:
            print(graph[i][j],end=" ")
    print()