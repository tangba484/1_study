n = int(input())
L = list(map(int,input().split()))
L.sort()
W=0
for i in L:
    if i > W+1:
        break
    W += i
print(W+1)