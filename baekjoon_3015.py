import sys
n = int(input())
cnt = 0
stack = []

for _ in range(n):
    x = int(sys.stdin.readline())
    V = (x, 1)
    while stack and stack[-1][0] <= x:
        cnt += stack[-1][1]
        if stack[-1][0] == x:
            V = (x, stack[-1][1] + 1) 
        stack.pop()
    if stack:
        cnt += 1
    stack.append(V)

print(cnt)
