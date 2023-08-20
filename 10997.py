n = int(input())

def R(n):
    if n == 1:
        return ["*"]
    elif n == 2:
        return ["*****","*    ","* ***","* * *","* * *","*   *","*****"]
    
    r = R(n-1)
    h = len(r)
    w = len(r[0]) + 4
    s = []
    for i in range(h+4):
        if i ==0:
            s.append("*"*w)
        elif i == 1:
            s.append("*"+" "*(w-1))
        elif i == h+3:
            s.append("*"*w)
        elif i == h+2:
            s.append("*"+" "*(w-2)+"*")
        elif i == 2:
            s.append("* "+r[0]+"**")
        else:
            s.append("* "+ r[i-2] + " *")
    return s

a = R(n)
c=0
for i in a:
    if c == 1:
        print("*")
        c += 1
        continue
    print(i)
    c += 1