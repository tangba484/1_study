import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline
n,m,r = map(int,input().split())

graph={i:[] for i in range(1,n+1)}

for _ in range(m):
    a,b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

visited=[0 for _ in range(n+1)]

ans = [[0] for _ in range(n+1)]
c = 1
def dfs (r,G):
    global c
    G.sort(reverse=True)
    visited[r] = 1
    ans[r] = [c]
    for i in graph[r]:
        if not visited[i]:
            c += 1
            dfs(i,graph[i])
dfs(r,graph[r])
for i in range(1,n+1):
    print(*ans[i])

