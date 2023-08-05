n,k = map(int,input().split())
l = list(map(int,input().split()))
ans = 0

p =[]

for i in range(k):
    t = l[i]
    if t in p:
        continue
    if len(p) < n:
        p.append(t)
        continue
    idx = 0
    for m in range(n):
        cnt = 9999
        for j in range(i+1,k):
            if p[m] == l[j]:
                cnt = j
                break
        if cnt > idx:
            e = m
            idx = cnt
    ans += 1
    p[e] = l[i]
print(ans)

