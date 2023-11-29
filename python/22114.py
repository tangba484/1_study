n,k = map(int,input().split())
l = list(map(int,input().split()))

start,end = 0,0
cnt,flag,index = 1,0,0
ans =[]
while 1:
    if end == n-1 or start ==n-1:
        break

    if l[end] <=k:
        cnt += 1
        end += 1
    else:
        if flag%2==0:
            flag += 1
            cnt += 1
            index = end
            end += 1
        else:
            flag += 1
            ans.append(cnt)
            start = index + 1
            end = start
            cnt = 1
            index = 0
if ans:
    print(max(max(ans),cnt))
else:
    print(cnt)

