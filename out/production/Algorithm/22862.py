n,k = map(int,input().split())
L = list(input().split())
for i in range(n):
    if L[i][-1] in "02468":
        L[i] = True
    else:
        L[i] = False

odd_cnt = [0]*n
c = 0
for i in range(n):
    if L[i] == False:
        c += 1
    odd_cnt[i] = c

left,right = 0,0
cnt = 0
while left < n:
    
    while cnt <= k:
        if L[right] == False:
            cnt += 1
        