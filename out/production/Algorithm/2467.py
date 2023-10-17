n= int(input())

L= list(map(int,input().split()))
L.sort()
left = 0
right = n-1

ans = (L[left],L[right])
diff = abs(L[left]+L[right])
while left < right:
    now_diff = (L[left]+L[right])
    
    if abs(now_diff) <= diff :
        ans = (L[left],L[right])
        diff = abs(now_diff)
    
    if now_diff ==0:
        break
    elif now_diff < 0:
        left +=1
    else:
        right -=1
print(*ans)