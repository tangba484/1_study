import heapq as hq
import sys
n = int(input())
l =[]
for _ in range(n):
    l.append(list(map(int,sys.stdin.readline().split())))
l.sort()

H = [0]

for x,y in l:
    if H[0] <= x:
        hq.heappop(H)
        hq.heappush(H,y)
    else:
        hq.heappush(H,y)
print(len(H))