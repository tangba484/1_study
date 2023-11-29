from collections import deque
start , end = map(int,input().split())
visited = [0]*(100001)

q = deque([start])
visited[start] = 0
ans = 0
while q:
    now = q.popleft()
    if now == end:
        ans += 1
        continue
    if 0<= now -1:
        if not visited[now-1] or visited[now-1]>=visited[now] + 1:
            q.append(now-1)
            visited[now-1] = visited[now] + 1
    if  now +1 <100001:
        if not visited[now+1] or visited[now+1]>=visited[now] + 1:
            q.append(now+1)
            visited[now+1] = visited[now] + 1
    if 2*now <100001:
        if not visited[2*now] or visited[2*now]>=visited[now] + 1:
            q.append(2*now)
            visited[2*now] = visited[now] + 1

print(visited[end])
print(ans)