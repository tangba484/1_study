n = int(input())
num = int(input())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

arr = [[0 for _ in range(n)] for _ in range(n)]
dir = 0
cnt = 1
rep = 1
x, y = n // 2, n // 2
Y, X = 0, 0
while cnt <= n ** 2:
    for _ in range(2):
        for _ in range(rep):
            if cnt <= n ** 2:
                arr[y][x] = cnt
                x += dx[dir]
                y += dy[dir]
                cnt += 1
        dir = (dir + 1) % 4
    rep += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
        if arr[i][j] == num:
            Y = i
            X = j
    print()
print(Y + 1, X + 1)