n = int(input())

k = 0
if n==1:
    print(1)
else:

    while 1:
        k+= 1
        if 2**k > n:
            k -= 1
            break
    print(k)