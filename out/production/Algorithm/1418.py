n = int(input())
k = int(input())

l = [i+1 for i in range(n)]
l = [0] + l
res = l[:]
for i in range(2,n):
    if l[i] != 0:
        for j in range(2*i,n+1,i):
            l[j] = 0
            res[j] = i


ans = 0
for i in res:
    if i <= k:
        ans += 1
print(ans-1)