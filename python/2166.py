n = int(input())
l = [i for i in range(1, n + 1)]
c = []
while len(l) != 1:
    c.append(l.pop(0))
    l.append(l.pop(0))
for i in c:
    print(i, end=' ')
print(l[0])