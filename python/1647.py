v,e = map(int,input().split())

E=[]

for _ in range(e):
    E.append(list(map(int,input().split())))

E = sorted(E,key = lambda x:x[2])

parent=[i for i in range(v+1)]

def find_parent(x):
    if x == parent[x]:
        return x
    return find_parent(parent[x])

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a>b:
        a,b =b,a
    parent[b] = a

ans = 0
M = 0
for a,b,c in (E):
    if find_parent(a) != find_parent(b):
        union(a,b)
        ans += c
        M = c
print(ans-M)