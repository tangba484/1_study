n = int(input())
k = int(input())

start,end = 0,n*n + 1

while start +1 < end:
    mid = (start + end)//2
    
    cnt = 0
    for i in range(1,n+1):
        cnt += min(mid//i,n)
    
    if cnt >= k:
        end = mid
    elif cnt < k:
        start = mid
print(start+1)