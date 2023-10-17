n,k = map(int,input().split())

l =[0]
a,b = map(int,input().split())
for _ in range(n-1):
    x,y = map(int,input().split())
    l.append(abs(x-a)+abs(y-b))
    x,y = a,b
# 막막하군 ..