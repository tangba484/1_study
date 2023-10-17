import sys

n = int(input())

g = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def rrr(g):
    global n
    if len(g) == 1:
        return g
    a = [[] for _ in range(n//2)]
    
    for i in range(n//2):
        for j in range(n//2):
            b =[]
            for x in range(2):
                for y in range(2):
                    b.append(g[2*i+x][2*j+y])
            b.sort()
            a[i].append(b[-2])
    n = n//2
    return rrr(a)

print(rrr(g)[0][0])