r,c = map(int,input().split())

graph=[]
for _ in range(r):
    graph.append(input())

result = []
def check(x,y):
    if x==0 or (x>=1 and graph[x-1][y]=="#"):
        s=""
        while x != r:
            s += graph[x][y]
            x += 1
            if x == r or graph[x][y] == "#":
                break
        if len(s)>=2:
            result.append(s)
def check1(x,y):
    if y==0 or (y>=1 and graph[x][y-1] == "#"):
        s=""
        while y != c :
            s += graph[x][y]
            y += 1
            if y == c or graph[x][y] == "#":
                break
        if len(s) >=2:
            result.append(s)

for i in range(r):
    for j in range(c):
        if graph[i][j] != "#":
            check(i,j)
            check1(i,j)
print(sorted(result)[0])