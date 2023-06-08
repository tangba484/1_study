a,b,c = map(int,input().split())

k = 1

while k <= c:
    if a >= 2*b:
        a=a-1
        k+=1
    else:
        b = b-1
        k+=1
print(min(int(a/2),b))