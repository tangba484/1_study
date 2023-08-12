import sys,heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph=[[]for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
start,end = map(int,input().split())

visited=[-1]*(n+1)
def dij(start):
    inf = float('inf')
    distance = [inf]*(n+1)
    distance[start] = 0
    H = [[0,start]]
    while H:
        x,y = heapq.heappop(H)
        if distance[y] < x:
            continue
        for a,b in graph[y]:
            C = b + x
            if C < distance[a]:
                distance[a] = C
                visited[a] = y
                heapq.heappush(H,[C,a])    
    
    cur = end
    box=[]
    while cur != start:
        box.append(cur)
        cur = visited[cur]
    box.append(start)
    return distance,box[::-1]
a,b = dij(start)
print(a[end])
print(len(b))
for i in b:
    print(i,end=" ")