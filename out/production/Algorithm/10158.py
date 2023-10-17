w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())

x = p + t%(2*w)
y = q + t%(2*h)
if x>w:
    x = 2*w-x
if x<0:
    x = -x
if y > h:
    y = 2*h - y
if y<0:
    y = -y
print(x,y)