n = int(input())

a = list(map(int,input().split()))
b = sorted(a)
result = [0] * n

for i in range(n):
  idx = b.index(a[i])
  result[i] = idx
  b[idx] = -1
print(*result)