n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int,input().split())))
l.sort()
for i in range(n):
    l[i] = l[i][1]

stack = [l[0]]
ls = 1

for i in range(1,n):
    if stack[-1] < l[i]:
        stack.append(l[i])
        ls += 1
    else:
        start = -1
        end = ls
        mid = (start+end)//2
        while start + 1 < end:
            mid = (start+end)//2
            if stack[mid] < l[i]:
                start = mid
            else:
                end = mid
        stack[end] = l[i]

print(n - len(stack))