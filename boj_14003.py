n = int(input())
l = list(map(int,input().split()))

stack = [l[0]]
length = 1
idx = [[0,0]]
for i in range(1,n):
    if l[i] > stack[-1]:
        stack.append(l[i])
        length += 1
        idx.append([length-1,i])
    else:
        target = l[i]
        start = 0
        end = length

        while start + 1 < end:
            mid = (start + end)//2
            if target < stack[mid]:
                end = mid
            else:
                start = mid
        if target > stack[start]:
            stack[end] = target
            idx.append([end,i])
        else:
            stack[start] = target
            idx.append([start,i])

k = len(stack) - 1
print(k+1)
ans = []
while idx and k >=0:
    x,y = idx.pop()
    if x == k:
        ans.append(l[y])
        k -= 1

print(*ans[::-1])