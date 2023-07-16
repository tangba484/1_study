from itertools import combinations as cb

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
home=[]
chiken = []
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            home.append([i,j])
        if g[i][j] == 2:
            chiken.append([i,j])

dist  = float("inf")
CB = cb(chiken,m)


# print(home,"home")
# print(chiken,"chicken")

for i in CB:
    cnt = 0
    for h in home:
        c = 99999
        for x in i:
            c = min(c,abs(x[0]-h[0])+abs(x[1]-h[1]))
        cnt += c
    dist = min(dist,cnt)
print(dist)
        