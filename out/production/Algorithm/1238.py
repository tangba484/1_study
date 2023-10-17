import sys,heapq
input = sys.stdin.readline
n,m,x = map(int,input().split())
graph=[[]for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

def dij(start):
    inf = float('inf')
    distance = [inf]*(n+1)
    distance[start] = 0
    h = [[0,start]]

    while h:
        x,y = heapq.heappop(h)
        if x > distance[y]:
            continue
        for next_idx,cost in graph[y]:
            C = cost + x
            if distance[next_idx] > C:
                distance[next_idx] = C
                heapq.heappush(h,[C,next_idx])
    return distance

result=[]
back_home = dij(x)
for start in range(1,n+1):
    result.append(dij(start)[x] + back_home[start])
print(max(result))
