from collections import deque
n = int(input())
l = (list(map(int,input().split())))
L=[]
for i in range(1,n+1):
    L.append([i,l[i-1]])
L = deque(L)
ans=[]


while L:
    x,y = L[0]
    L.popleft()
    ans.append(x)
    if y >0:
        L.rotate(-(y-1))
    else:
        L.rotate(-y)


print(*ans)