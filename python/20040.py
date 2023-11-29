n,m = map(int,input().split())

parent = [i for i in range(n)]

def find_parent(x):
    if x == parent[x]:
        return x
    
    return find_parent(parent[x])
def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a >= b:
        parent[a] = b
    else:
        parent[b] = a
flag = 0
for i in range(m):
    a,b = map(int,input().split())
    if flag >0:
        continue
    if find_parent(a) != find_parent(b):
        union(a,b)
    else:
        flag = i + 1
print(flag)
