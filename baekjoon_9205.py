from collections import deque
def d(X1,X2):
    if abs(X2[0]-X1[0]) +abs(X2[1]-X1[1]) <= 1000:
        return 1
    else:
        return 0

t = int(input())
for _ in range(t):
    n = int(input())
    l=[]

    for i in range(n+2):
        l.append(list(map(int,input().split())))

    visited = [0]*(n+2)
    q = deque([l[0]])
    visited[0] = 1

    def bfs():
        
        while q:
            X = q.popleft()
            if X == l[-1]:
                return "happy"
            for i in range(n+2):
                if d(X,l[i]) and not visited[i]:
                    visited[i] = 1
                    q.append(l[i])
        return "sad"
    print(bfs())
    