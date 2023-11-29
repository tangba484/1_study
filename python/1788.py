n = int(input())
l = [0, 1]
for i in range(2, abs(n) + 1):
    l.append((l[i - 1] + l[i - 2]) % 1000000000)
if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(l[abs(n)]% 1000000000)