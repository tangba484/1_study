
n = int(input())
l = list(map(int,input().split()))
left , right = 0,n-1
x = abs(l[left]+l[right])
ans = x
while left<right:
    y = l[left] + l[right]

    if abs(y) <= x:
        x = abs(y)
        ans = y
    
    if y == 0:
        break
    elif y<0:
        left += 1
    else:
        right -= 1
print(ans)
