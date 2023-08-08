import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
q = deque([])
graph=[[]for _ in range(n+1)]
inDegree = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    inDegree[b] += 1
for i in range(1,n+1):
    if inDegree[i] == 0:
        q.append(i)

ans = []
while q:
    x = q.popleft()
    ans.append(x)
    for i in graph[x]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            q.append(i)
print(*ans)