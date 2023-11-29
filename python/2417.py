n= int(input())

start,end = -1,n+1

while start + 1 < end:
    mid = (start + end)//2
    
    if mid**2 >=n:
        end = mid
    else:
        start = mid
print(end)