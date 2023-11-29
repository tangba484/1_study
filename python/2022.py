x,y,c = map(float,input().split())

start,end = 0,min(x,y)

while start +10**(-3) < end:
    mid = (start + end)/2
    
    a = (x**2-mid**2)**(1/2)
    b = (y**2-mid**2)**(1/2)
    h = a*b/(a+b)
    
    if h >= c:
        start = mid
    else:
        end = mid
print(end)