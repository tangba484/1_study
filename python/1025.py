N , M = map(int,input().split())

g = [list(map(int,list(input()))) for _ in range(N)]

answer = -1

DX = [i for i in range(-N,N+1)]
DY = [i for i in range(-M,M+1)]

for i in range(N):
    for j in range(M):
        for dx in DX:
            for dy in DY:
                n = 0
                x,y = i,j
                while 0<= x <N and 0<=y<M:
                    n += g[x][y]
                    if dx==0 and dy ==0:
                        break
                    if n**(1/2) == int(n**(1/2)):
                        answer = max(answer,n)
                    x += dx
                    y += dy
                    n *= 10
                
print(answer)