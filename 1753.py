import sys
import heapq
v,e = map(int,input().split())
start = int(input())
visited =[0]*(v+1)
graph = [[]for _ in range(v+1)]
INF = float("inf")
dist = [INF]*(v+1)
for _ in range(e):
    u,V,w = map(int,sys.stdin.readline().split())
    graph[u].append([V,w])

def w():
    m = INF
    index = 0
    for i in range(1,v+1):
        if dist[i] < m and not visited[i]:
            m = dist[i]
            index = i
    return index

def dij(start):
    dist[start] = 0
    visited[start] = 1
    for j in graph[start]:
        dist[j[0]] = j[1]
    for i in range(v-1):
        now = w()
        visited[now] = 1
        for j in graph[now]:
            cost = dist[now] + j[1]
            if cost < dist[j[0]]:
                dist[j[0]] = cost

dij(start)
for i in range(1,v+1):
    print(dist[i])