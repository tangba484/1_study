n = int(input())
stack = []
cnt = 0
for _ in range(n):
    n = int(input())
    V = (n,1)

    while stack and stack[-1][0] <= n:
        cnt += stack[-1][1]
        if stack[-1][0] == n:
            V = (n,stack[-1][1] + 1)
        stack.pop()
    
    stack.append(V)
print(cnt)