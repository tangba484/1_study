from itertools import combinations_with_replacement as cr

n = int(input())
l = [int(input()) for _ in range(n)]
l.sort()

X = set()

for x, y in cr(range(n), 2):
    X.add(l[x] + l[y])

X = sorted(X)

def R():
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            if l[i] - l[j] in X:
                return l[i]
print(R())