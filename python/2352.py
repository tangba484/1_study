n = int(input())
l = list(map(int,input().split()))
stack = [l[0]]

start ,cnt = 0,0

for i in range(1,n):
    x = stack[-1]
    if l[i] > x:
        stack.append(l[i])
        cnt += 1
    else:
        start = 0
        end = cnt
        while start <= end:
            mid = (start+end)//2

            if stack[mid] < l[i]:
                start = mid + 1
            else:
                end = mid - 1
        stack[start] = l[i]

print(len(stack))