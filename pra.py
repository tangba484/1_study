N = int(input())
F = int(input())
for i in range(100):
    new_N = N // 100 * 100 + i 
    if new_N % F == 0:
        print(str(new_N)[-2:].zfill(2))
        break