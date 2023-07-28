import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
l =[]
while 1:
    try:
        l.append(int(input()))
    except:
        break


def r(l):
    if not l:
        return []
    
    root = l[0]
    index = 1
    n = len(l)
    while index < n and l[index]<root:
        index += 1
    
    left = r(l[1:index])
    right = r(l[index:])

    return print(root)

r(l)