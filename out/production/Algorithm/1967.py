import sys
sys.setrecursionlimit(10**7)
n = int(input())
graph=[[]for _ in range(n+1)]

for _ in range(n-1):
    x,y,c = map(int,input().split())
    graph[x].append([y,c])
    graph[y].append([x,c])
dist = [-1 for _ in range(n+1)]
dist[1] = 0
def dfs(start):
    for i in graph[start]:
        idx,c = i[0],i[1]
        if dist[idx]==-1:
            dist[idx] = dist[start] + c
            dfs(idx)
    return dist
result = (dfs(1))
r = result.index(max(result))
dist = [-1 for _ in range(n+1)]
dist[r]=0
print(max(dfs(r)))


