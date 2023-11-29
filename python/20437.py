import copy
t = int(input())
for _ in range(t):
    s = input()
    k = int(input())
    n = len(s)
    D = {}
    for i in range(97,123):
        D[chr(i)] = [0,[]]

    for i in range(n):
        D[s[i]][0] += 1
        D[s[i]][1].append(i)

    check =[]
    for x,y in D.items():
        if y[0] >= k:
            check.append([x,y])
    result =[]
    for i in check:
        x = i[1][0]
        y = i[1][1]
        for j in range(x-k+1):
            result.append([y[j+k-1]-y[j]+1,s[y[j]:y[j+k-1]+1]])

    result = sorted(result,key = lambda x :(x[0]))
    
    if result:
        print(result[0][0],result[-1][0])
    else:
        print(-1)
            
        
    
    