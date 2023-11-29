N, K = map(int,input().split())
L = list(map(int,input().split()))
cnt = 0
for i in range(2*N):
    L[i] = [L[i],0]

step = 0
def move(L):
    return [L[-1]]+L[:-1]

while cnt < K:
    step += 1
    L = move(L)
    if L[N-1][1] == 1:
        L[N-1][1] = 0
    for i in range(N-2,-1,-1):
        if L[i][1] == 1 and L[i+1][1] == 0 and L[i+1][0] >= 1:
            L[i][1] = 0
            L[i+1][1] = 1
            L[i+1][0] -= 1
            if L[i+1][0] == 0:
                cnt +=1
    if L[N-1][1] == 1:
        L[N-1][1] = 0
    if L[0][0] > 0 and L[0][1] ==0:
        L[0][1] = 1
        L[0][0] -= 1
        if L[0][0] == 0:
            cnt += 1

print(step)
    
    
            
            