n = int(input())

x,y = map(int,input().split())

m = int(input())
l = []
for _ in range(m):
    l.append(int(input()))
stack=[[x,y,0]]
for t in l:
    S = []
    while stack:
        a,b,c = stack.pop()
        S.append([t,b,c+abs(a-t)])
        S.append([a,t,c + abs(b-t)])
    stack = S
ans = float("inf")
for i in stack:
    ans = min(ans,i[2])
print(ans) # 왜 풀리지 ? 왜 메모리초과가 안나지 ???