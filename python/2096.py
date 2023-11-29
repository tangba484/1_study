import sys
input = sys.stdin.readline
n = int(input())


dpM =[0,0,0]
dpm =[0,0,0]

for _ in range(n):
    l = (list(map(int,input().split())))

    a = max(dpM[0]+l[0],dpM[1]+l[0])
    b = max(l[1]+dpM[0],l[1]+dpM[1],l[1]+dpM[2])
    c = max(dpM[1]+l[2],dpM[2]+l[2])
    x = min(dpm[0]+l[0],dpm[1]+l[0])
    y = min(l[1]+dpm[0],l[1]+dpm[1],l[1]+dpm[2])
    z = min(dpm[1]+l[2],dpm[2]+l[2])
    dpM,dpm=[a,b,c],[x,y,z]


print(max(dpM),min(dpm))
