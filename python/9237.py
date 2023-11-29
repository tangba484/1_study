n = int(input())

l = list(map(int, input().split()))
l.sort(reverse=True)

ans = []
for i in range(n):
    ans.append(l[i]+ 1 + i)

print(max(ans) + 1)