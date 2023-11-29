n,atk = map(int,input().split())
H = 0

start = 1
end = 0
atk2=atk
l=[]
for _ in range(n):
    a,b,c = map(int,input().split())
    l.append([a,b,c])
    if a == 1:
        end += int(((c-0.1)//atk2 )*(b))
    elif a == 2:
        atk2 += b

def check(hp,atk):
    # print(hp,atk)
    max_hp = hp
    for a,b,c in l:
        if a == 1:
            hp -= int(((c-0.1)//atk)*b)
            if hp <= 0:
                return False
        elif a == 2:
            atk += b
            if hp + c >= max_hp:
                hp = max_hp
            else:
                hp += c
    return True
end+=1
while start + 1 < end:
    mid = (start + end) // 2
    if check(mid,atk):
        end = mid
    else:
        start = mid
print(end)