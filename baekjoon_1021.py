from collections import deque
n,m = map(int,input().split())
l = deque(list(map(int,input().split())))
x1,x2,x3 = 0,0,0
q = deque(range(1,n+1))


while l:
    target = l.popleft()
    if target == q[0]:
        x1 += 1
        q.popleft()
        n -= 1
    else:
        I = q.index(target)
        if len(q)//2 >= I:
            while 1:
                x = q.popleft()
                if x == target:
                    break
                else:
                    q.append(x)
                    x2 += 1                  
        else:
            while 1:
                x = q.pop()
                if x == target:
                    x3 += 1
                    break
                else:
                    q.appendleft(x)
                    x3 += 1

print(x2+x3)
