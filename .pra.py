while 1:
    x,y,z = map(int,input().split())
    if (x,y,z) ==(0,0,0):
        break
    T = sorted([x,y,z])
    
    if T[2] >= T[1] + T[0]:
        print("Invalid")
        continue
    if T[0] == T[1] and T[1]==T[2]:
        print("Equilateral")
    elif T[0]==T[1] or T[1]==T[2]:
        print("Isosceles")
    else:
        print("Scalene")