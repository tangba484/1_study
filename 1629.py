a,b,c = map(int,input().split())

def R(a,b,c):
    if b == 1:
        return a%c
    
    tmp = R(a,b//2,c)
    
    if b % 2 == 0:
        return tmp*tmp%c
    else:
        return tmp*tmp*a%c
print(R(a,b,c))
