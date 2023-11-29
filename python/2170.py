import sys
from collections import deque
n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
a = deque(sorted(a,key = lambda x:(x.sort(),x[0])))
b = deque([[a[0][0],a[0][1]]])

while a:
    x,y = a.popleft()
    i,j = b.popleft()
    if x==i and y==j:
        b.appendleft([i,j])
    elif j >= x:
        if y-i >= j-i:
            b.appendleft([i,y])
        else:
            b.appendleft([i,j])
    else:
        b.appendleft([i,j])
        b.appendleft([x,y])

ans =0
for x,y in b:
    ans += y-x
print(ans)