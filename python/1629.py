a,b,c = map(int,input().split())

def R(a,b,c):
    if b == 1 :
        return a%c
    
    ans = R(a,b//2,c)
    if b%2 == 1:
        return ans*ans*a%c
    else:
        return ans*ans%c
print(R(a,b,c))