n = int(input())
l = list(map(int,input().split()))
a = [0 for i in range(max(l) + 1)]
for i in l:
    a[i] = i
ans=[0 for i in range(max(l) + 1)]
k = len(a)

for i in range(1,k):
    if a[i] > 0:
        for j in range(2*i,k,i):
            if a[j] > 0:
                if a[j]%a[i] == 0:
                    ans[i] += 1
                    ans[j] -= 1
for i in l:
    print(ans[i],end = " ")