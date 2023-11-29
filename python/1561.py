n,m = map(int,input().split())
l = list(map(int,input().split()))


start,end = 0,n*30 + 1
if n <=m:
    print(n)
else:
    while start + 1 < end:
        mid = (start + end)//2
        
        cnt = m
        for i in range(m):
            cnt += mid//l[i]
            if cnt >=n:
                break
        
        if cnt >=n:
            end = mid
        else:
            start = mid
    result = start + 1

    cnt = m
    for i in l:
        cnt += (result-1)//i
    
    for i in range(m):
        if result%l[i] == 0:
            cnt += 1
        if cnt == n:
            print(i+1)
            break