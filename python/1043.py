import sys
input = sys.stdin.readline
n,m = map(int,input().split())
known = list(map(int,input().split()))
if known[0] == 0:
    for _ in range(m):
        party = list(map(int,input().split()))
    print(m)
else:
    D={}
    for i in range(n):
        D[i+1] = set()
    P = []
    for _ in range(m):
        party = list(map(int,input().split()))
        k = party[0]
        party_list = party[1:]
        P.append(party_list)
        for i in range(k):
            for j in range(k):
                if i != j:
                    D[party_list[i]].add(party_list[j])
    graph=[[]for _ in range(n+1)]
    for x,y in D.items():
        graph[x] = list(y)
    visited=[0]*(n+1)
    k = known[0]
    stack = known[1:]

    while stack:
        x = stack.pop()
        visited[x] = 1
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                stack.append(i)


    cnt = 0
    for p in P:
        for x in p:
            if visited[x] == 1:
                cnt += 1
                break
    print(m-cnt)