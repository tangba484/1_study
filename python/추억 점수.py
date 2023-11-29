def solution(name, yearning, photo):
    result =[]
    n = len(name)
    D={}
    for i in range(n):
        D[name[i]] = yearning[i]
    for p in photo:
        ans=0
        for i in p:
            if i in D:
                ans += D[i]
        result.append(ans)
    return (result)