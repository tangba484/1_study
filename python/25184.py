n = int(input())

for i in range(n // 2, 0, -1):
    print(i, i + n // 2, end=" ")

if n % 2 == 1:
    print(n)
