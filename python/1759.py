L , C = map(int,input().split())
d = sorted(list(input().split()))
def check(s):
    a = 0
    b = 0
    for i in range(L):
        if s[i] in "aeiou":
            a += 1
        else:
            b += 1
        if a>=1 and b>=2:
            return True
    return False

def back(s,Len,idx):
    
    if Len == L and check(s):
        print("".join(s))
        return
    for i in range(idx,C):
        back(s+[d[i]],Len+1,i+1)

back([],0,0)