n = int(input())
l = list(map(int,input().split()))

dpu = [0]*(n+1)
dpd = [0]*(n+1)
dpu[0] = 1
dpd[0] = 1
u,d = l[0],l[0]
for i in range(1,n):
    if l[i] >= u:
        u = l[i]
        dpu[i] = dpu[i-1]+1
    else:
        u = l[i]
        dpu[i] = 1
    
    if l[i] <= d:
        d = l[i]
        dpd[i] = dpd[i-1] + 1
    else:
        d = l[i]
        dpd[i] = 1

print(max(max(dpd),max(dpu)))