import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m,w = map(int,input().split())
    road=[]
    for _ in range(m):
        s,e,t = map(int,input().split())
        road.append([s,e,t])
        road.append([e,s,t])
    for _ in range(w):
        s,e,t = map(int,input().split())
        road.append([s,e,-t])
    inf = 1987654321
    distance = [inf]*(n+1)
    def bf(start):
        distance[start] = 0
        for i in range(n):
            for x,y,c in road:
                if distance[y] > distance[x] + c:
                    distance[y] = distance[x] + c
                    if i == n-1:
                        return "YES"
        return "NO"
    print(bf(1))