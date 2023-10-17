t = int(input())
for _ in range(t):
    a,b = map(int,input().split())

    box  = []
    i = 1
    while 1:
        if (a**i) % 10 in box:
            break
        else:
            box.append((a**i) % 10)
        i += 1
    k = len(box)
    x = ( box[b%k - 1])
    if x == 0:
        print(10)
    else:
        print(x)