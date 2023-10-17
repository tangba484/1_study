def gcd(a,b):

    if b == 0:
        return a
    else:
        return gcd(b,a%b)
def solution(arrayA, arrayB):
    
    x,y = 0,0
    
    for i in range(len(arrayA)):
        x = gcd(arrayA[i],x)
    for i in range(len(arrayB)):
        y = gcd(arrayB[i],y)
    
    for i in arrayA:
        if i%y == 0:
            y=0
            break
    for i in arrayB:
        if i%x == 0:
            x =0
            break
    return (max(x,y))
    
    