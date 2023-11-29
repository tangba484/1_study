import sys
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
inf = float('inf')
dist = [inf]*(n+1)
for _ in range(m):
    x,y,z, = map(int,sys.stdin.readline().split())
    graph[x].append([y,z])
start , target = map(int,input().split())

def w():
    m = inf
    index = 0
    for i in range(1,n+1):
        if dist[i]<m and not visited[i]:
            m = dist[i]
            index = i
    return index

def dij(start):
    dist[start] = 0
    visited[start] = 1
    for j in graph:
        j.sort(key=lambda x:-x[1])
    for j in graph[start]:
        dist[j[0]] = j[1]
    for i in range(n-1):
        now = w()
        visited[now] = 1
        for j in graph[now]:
            cost = dist[now] + j[1]
            if cost < dist[j[0]]:
                dist[j[0]] = cost

dij(start)
print(dist[target])