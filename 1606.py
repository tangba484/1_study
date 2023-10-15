
x, y = map(int, input().split())
res = 1
for i in range(1, x + y + (1 if y == 0 else 0)):
    res += 6 * i
print(res + y)