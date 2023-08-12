n = int(input())

l = list(map(int,input().split()))
b = list(map(int,input().split()))
c =[]

for i in range(4):
    if i == 0:
        for _ in range(b[i]):
            c.append("+")
    elif i == 1:
        for _ in range(b[i]):
            c.append("-")
    elif i == 2:
        for _ in range(b[i]):
            c.append("*")
    elif i == 3:       
        for _ in range(b[i]):
            c.append("/")
result = []
# n개의 숫자 존재 , n-1 개의 연산자 존재
def back(x,a,b):
    if a == n:
        return result.append(x)
    
    for i in range(n-1):
        if i not in b:
            if c[i] == "+":
                back(x+l[a],a+1,b+[i])
            elif c[i] == "-":
                back(x-l[a],a+1,b+[i])
            elif c[i] == "*":
                back(x*l[a],a+1,b+[i])
            else:
                if x <= 0:
                    back(-(-x//l[a]),a+1,b+[i])
                else:
                    back(x//l[a],a+1,b+[i])

back(l[0],1,[])

print(max(result))
print(min(result))