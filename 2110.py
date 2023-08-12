import sys
N,C = map(int,input().split())
L=[]
for _ in range(N):
    L.append(int(sys.stdin.readline()))
L.sort()

start = 1
end = L[-1]
answer=0
if C ==2:
    print(L[-1]-L[0])
else:
    while start < end:
        mid = (start+end)//2
        ls = L[0]
        cnt=1
        for i in range(N):
            if L[i] - ls >=mid:
                cnt +=1
                ls = L[i]
        
        if cnt >=C:
            answer = mid
            start = mid +1
        else:
            end = mid 
    print(answer)