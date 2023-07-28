n,m,r = map(int,input().split())
t = list(map(int,input().split()))
INF = float("inf")
graph =[[INF for _ in range(n+1)]for _ in range(n+1)]
for _ in range(r):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1,n+1):
    for i in range(1,n+1):
        graph[i][i] = 0
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
ans = 0
for i in graph:
    s=0
    for j in range(1,n+1):
        if i[j] <=m:
            s+=t[j-1]
    ans = max(s,ans)
print(ans)