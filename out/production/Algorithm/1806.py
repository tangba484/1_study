n,s = map(int,input().split())
L = list(map(int,input().split()))

start = 0
end = 0
S=L[0]
ans = 999999

while True:
    if S <s:
        end +=1
        if end==n:
            break
        S += L[end]
    else:
        ans = min(ans,end-start+1)
        S -= L[start]
        start +=1
print(ans if ans!=999999 else 0)