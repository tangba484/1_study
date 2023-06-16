n = int(input())
my = list(map(int,input().split()))

m = int(input())
check = list(map(int,input().split()))

D ={}

for i in my:
    D[i] = 1

for i in check:
    if i in D:
        print(1,end=" ")
    else:
        print(0,end=" ")