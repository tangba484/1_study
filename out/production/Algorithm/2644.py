from collections import deque
n = int(input())
x,target = map(int,input().split())

g =[[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(int(input())):
    t1,t2 = map(int,input().split())
    g[t1].append(t2)
    g[t2].append(t1)

for i in range(len(g[x])):
    g[x][i] = [g[x][i],0]

q = deque(g[x])

visited[x] = 1

def bfs():
    while q:
        a,cnt = q.popleft()
        if a == target:
            return cnt + 1
        
        for i in g[a]:
            if not visited[i] and g[i]:
                visited[i] = 1
                q.append([i,cnt+1])
    return -1
print(bfs())