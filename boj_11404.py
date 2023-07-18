import sys,heapq
n = int(input())
m = int(input())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])

def P(a):
    for i in a:
        if i == float("inf"):
            print(0,end=" ")
        else:
            print(i,end=" ")
    return print()
INF = float("inf")
for start in range(1,n+1):
    def dij(start):
        dist = [INF]*(n+1)
        dist[start] = 0
        q = []
        heapq.heappush(q,[dist[start],start])
        while q:
            d,next_idx = heapq.heappop(q)
            if dist[next_idx] < d:
                continue
            for next_t,next_d in graph[next_idx]:
                D = d+next_d
                if D < dist[next_t]:
                    dist[next_t] = D
                    heapq.heappush(q,[D,next_t])
        return P(dist[1:])
    dij(start)
    