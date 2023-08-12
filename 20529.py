from itertools import combinations as comb


def d(a,b):
    d = 0
    for i in range(4):
        if a[i] != b[i]:
            d +=1
    return d
t = int(input())
for _ in range(t):
    n = int(input())
    D={}
    L = list((input().split(" ")))
    flag = 0
    for i in L:
        if i not in D:
            D[i] = 1
        else:
            D[i] += 1
        if D[i]  >= 3:
            flag = 1
    
    if flag == 1:
        print(0)
        continue

    C = comb(range(len(L)),3)
    aa = 100
    
    for x,y,z in C:
        m = d(L[x],L[y]) + d(L[y],L[z]) + d(L[z],L[x])
        if m < aa:
            aa = m
    if aa == 100:
        print(0)
    else:
        print(aa)