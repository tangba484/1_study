import sys
G = [ list(map(int,list(input())))  for _ in range(9)]

vst1=[[False for _ in range(9)] for _ in range(9)]
vst2=[[False for _ in range(9)] for _ in range(9)]
vst3=[[False for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        if G[i][j]>0:
            vst1[i][G[i][j]-1] = True
            vst2[j][G[i][j]-1] = True
            vst3[(i//3)*3 +j//3][G[i][j]-1] = True
flag =0
def back(x,y):
    global flag
    if x ==9:
        if flag ==0:
            flag = 1
            for i in G:
                print("".join(list(map(str,i))))
            sys.exit()
    if G[x][y]:
        back(x+(y+1)//9,(y+1)%9)
        return
    
    for i in range(9):
        if vst1[x][i] or vst2[y][i] or vst3[x//3*3 + y//3][i]:
            continue
        G[x][y] = i+1
        vst1[x][i] =True
        vst2[y][i] = True
        vst3[x//3*3 + y//3][i] = True
        back(x+(y+1)//9,(y+1)%9)
        G[x][y] = 0
        vst1[x][i] =False
        vst2[y][i] = False
        vst3[x//3*3 + y//3][i] = False
back(0,0)   
