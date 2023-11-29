n = int(input())
l = list(map(int,input().split()))

stack = [l[0]]
length = 1

for i in range(1,n):
    if l[i] > stack[-1]:
        stack.append(l[i])
        length += 1
    else:
        target = l[i]
        start = -1
        end = length - 1


        while start + 1 < end:
            mid = (start + end) // 2
            if stack[mid] < target:
                start = mid
            else:
                end = mid
        stack[end] = target
    # print(stack)
print(len(stack))