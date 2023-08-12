import sys


t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline())
    l = list(map(int,sys.stdin.readline().split()))
    ML = [0]*n
    for i in range(n-2,-1,-1):
        ML[i] = max(ML[i+1],l[i+1])

    p = 0
    for i in range(n):
        if l[i] < ML[i]:
            p += ML[i] - l[i]
    print(p)