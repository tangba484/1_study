a, b = map(int, input().split())
res = abs(a-b)
for _ in range(int(input())):
    k = int(input())
    if res > abs(k-b):
        res = abs(k-b)+1

print(res)