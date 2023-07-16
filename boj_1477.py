n,m,l = map(int,input().split())

if n == 0:
    print((l-1)//(m+1)+1)
else:
    a = list(map(int,input().split()))
    a.sort()
    a = [0] + a + [l]
    A = []
    for i in range(1,n+2):
        A.append(a[i]-a[i-1] -1)

    start ,end = 0,l
    while start + 1 < end:
        mid = (start + end)//2
        
        cnt = 0
        for i in A:
            cnt += i//mid
        
        if cnt > m:
            start = mid
        else:
            end = mid
    print(start+1)