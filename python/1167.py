import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
graph=[[]for _ in range(n+1)]
for _ in range(n):
    l = list(map(int,input().split()))
    k = (len(l)-2)//2
    for i in range(k):
        graph[l[0]].append([l[1+2*i],l[1+ 2*i+1]])
        # graph[l[1+2*i]].append([l[0],l[1+ 2*i+1]])

dist = [-1]*(n+1)
dist[1] = 0
def dfs(start):
    for x,y in graph[start]:
        if dist[x] == -1:
            dist[x] = y+dist[start]
            dfs(x)
    return dist
dfs(1)
start = dist.index(max(dist))
dist = [-1]*(n+1)
dist[start] = 0
print(max(dfs(start)))