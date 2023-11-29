n = int(input())
l = list(map(int,input().split()))
ans =[0]
c = 0
for i in range(n):
    x = l[i]
    if ans[-1] < x:
        ans.append(x)
        c += 1
    else:
        left,right = 0,c
        while left <= right:
            mid = (left + right)//2
            if ans[mid] <x:
                left = mid + 1
            else:
                right = mid - 1
        ans[left] = x

print(len(ans)-1)