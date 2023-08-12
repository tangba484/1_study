n = int(input())
l = list(map(int,input().split()))
l.sort()

flag = 0
ans = [3000000001]
for i in range(n-2):
    start,end = i,n-1
    if flag == 1:
        break

    if (abs(l[i]+l[i+1]+l[end])) <= abs(l[i]+l[end-1]+l[end]):
        X = abs(l[i]+l[i+1]+l[end])
    else:
        X = abs(l[i]+l[end-1]+l[end])
    start = i+1
    while start < end:
        Y = l[i] + l[start] + l[end]
        if abs(Y) <= X:
            if abs(Y) < abs(sum(ans)):
                ans = (l[i],l[start],l[end])
            # print((l[i],l[start],l[end]))
            X = abs(Y)
        if Y==0:
            flag = 1
            ans = (l[i],l[start],l[end])
            break
        elif Y<0:
            start += 1
        else:
            end -= 1
print(*ans)
