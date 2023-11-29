t = int(input())
l=[]
for _ in range(t):
    x = input()
    l.append(x)
    if x == "?":
        idx = _

box=[]
n = int(input())
for _ in range(n):
    x = input()
    if x in l:
        continue
    box.append(x)
if t == 1:
    print(box[0])
else:
    if 0<idx<t-1:
        left = l[idx-1][-1]
        right = l[idx+1][0]
        for x in box:
            if x[0] == left and x[-1] == right:
                print(x)
                break
    elif idx ==0:
        right = l[idx+1][0]
        for x in box:
            if x[-1] == right:
                print(x)
                break
    else:
        left = l[idx-1][-1]
        for x in box:
            if x[0] == left:
                print(x)
                break