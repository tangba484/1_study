from collections import deque

n = int(input())

q = deque([1])
visited = [[[],0] for _ in range(n+1)]

visited[1][0].append(1)
if n == 1:
    print(0)
    print(1)
else:
    while 1:
        x = q.popleft()
        if x == n:
            break
        if x*3 <= n :
            if visited[3*x][1] == 0:
                q.append(3*x)
                visited[3*x][0] = visited[x][0]+[x*3]
                visited[3*x][1] = visited[x][1] + 1
        if x*2 <= n :
            if visited[2*x][1] == 0:
                q.append(2*x)
                visited[2*x][0] = visited[x][0]+[x*2]
                visited[2*x][1] = visited[x][1] + 1   
        if x+1 <=n:
            if visited[x+1][1] == 0:
                q.append(x+1)
                visited[x+1][0] = visited[x][0]+[x+1]
                visited[x+1][1] = visited[x][1] + 1             
    print(visited[-1][1])
    print(*visited[-1][0][::-1])
