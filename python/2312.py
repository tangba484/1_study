t = int(input())
for _ in range(t):
    n = int(input())
    num = 2
    D = {}
    for i in range(n+1):
        D[i] = 0

    while 1:
        if n == 1:
            break
        if n % num != 0:
            num += 1
        else:
            n /= num
            D[num] += 1

    for i in D.items():
        if i[1] != 0:
            print(i[0], i[1])