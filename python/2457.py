n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int,input().split())))
l.sort()

flag = 0
S,E=[[3,1]],[[3,1]]
for i in l:
    x,y = E[-1][0],E[-1][1]
    s1,s2,e1,e2 = i[0],i[1],i[2],i[3]
    if (s1<x or (s1<=x and s2<=y)) and (e1>x or (e1>=x and e2>=y)):
        try:
            if (s1<E[-2][0] or (s1<=E[-2][0] and s2<=E[-2][1])):
                S.pop()
                E.pop()
                S.append([s1,s2])
                E.append([e1,e2])
            else:
                S.append([s1,s2])
                E.append([e1,e2])
        except:
            S.append([s1,s2])
            E.append([e1,e2])   
    if e1>11 or (e1>=11 and e2>30):
        flag = 1
        break
# print(S)
# print(E)
if flag == 1 and E[-1][0]>11 or (E[-1][0]>=11 and E[-1][1]>30):
    print(len(E)-1)
else:
    print(0)
