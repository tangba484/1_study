import sys
n,m = map(int,input().split())

l = []
for _ in range(n):
    l.append(int(sys.stdin.readline().rstrip()))
l.sort()

start = 0
end = l[-1]*m + 1

while start + 1 < end:
    mid = (start + end)//2
    
    cnt = 0
    for i in range(n):
        cnt += mid//l[i]
    
    if cnt >= m:
        end = mid
    else:
        start = mid
print(end)