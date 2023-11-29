n = int(input())
l=[int(input()) for _ in range(n)]
p=[]
n=[]

for i in l:
    if i <= 0:
        n.append(i)
    else:
        p.append(i)
        
n.sort();p.sort(reverse=True)

result_p=0
for i in range(len(p)//2+1):
    if len(p[2*i:(2*i+2)]) == 2:
        x,y = p[2*i:(2*i+2)]
        if x==1 or y == 1:
            result_p += x+y
        else:
            result_p += x*y
    else:
        x = p[2*i:(2*i+2)]
        try:
            result_p += x[0]
        except:
            continue
        
result_n=0
for i in range(len(n)//2+1):
    if len(n[2*i:(2*i+2)]) == 2:
        x,y = n[2*i:(2*i+2)]
        if x==0 or y == 0:
            result_n += x*y
        else:
            result_n += x*y
    else:
        x = n[2*i:(2*i+2)]
        try:
            result_n += x[0]
        except:
            continue
        
print(result_p + result_n)