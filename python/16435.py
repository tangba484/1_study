import sys

input =sys.stdin.readline

N, L = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

for t in h:
    if t > L:
        break
    elif t <= L:
        L += 1

print(L)