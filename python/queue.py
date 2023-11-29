from collections import deque as dq
import sys
n = int(input())
q = dq([])
for _ in range(n):
    X = list(sys.stdin.readline().split())
    if X[0] == "push":
        q.append(int(X[1]))
    if X[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    if X[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    if X[0] == "size":
        print(len(q))
    if X[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    if X[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)