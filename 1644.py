n = int(input())

p = [i for i in range(n+1)]
for i in range(2,n//2 + 1):
    if p[i] != 0:
        for j in range(2*i,n+1,i):
            p[j] = 0
p[1] = 0
p = list(set(p))
p = sorted(p)[1:]
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    k = len(p)
    cnt = 0
    start,end = 0,0
    s = p[start]
    while start < k :
        if s == n:
            cnt += 1
            s -= p[start]
            start += 1
        elif s>n:
            s -= p[start]
            start += 1
        elif s<n and end<k-1:
            end += 1
            s += p[end]
        if end == k-1:
            break

    if n in p:
        print(cnt + 1)
    else:
        print(cnt)