import sys
import heapq
input = sys.stdin.readline
n,e = map(int,input().split())
graph=[[]for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
v1,v2 = map(int,input().split())
def dij(start):
    distance = [float('inf') for _ in range(n+1)]
    distance[start] = 0
    h = [[0,start]]

    while h:
        dist,idx = heapq.heappop(h)
        if dist > distance[idx]:
            continue
        for next_idx,c in graph[idx]:
            cost = dist + c
            if cost < distance[next_idx]:
                distance[next_idx] = cost
                heapq.heappush(h,[cost,next_idx])
    return distance

a = dij(1)
b = dij(v1)
c = dij(v2)

ans = min(a[v1]+b[v2]+c[n],a[v2] + c[v1] + b[n])
print( -1 if ans==float('inf') else ans)