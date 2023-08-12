t = int(input())
def fp(X):
    if X == 1 or X == 0:
        return False
    for i in range(2,int(X**(1/2)) + 1):
        if X % i == 0:
            return False
    return True
for _ in range(t):
    n = int(input())
    
    while 1:
        if fp(n):
            print(n)
            break
        else:
            n += 1