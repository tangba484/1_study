def solution(places):
    def check(x,y):
        dx,dy=[1,-1,0,0],[0,0,1,-1]
        for i in range(4):
            if 0<=x+dx[i]<5 and 0<= y+dy[i]<5:
                if p[x+dx[i]][y+dy[i]] == "P":
                    return False
        dx,dy=[-1,-1,1,1],[-1,1,-1,1]
        for i in range(4):
            if 0<=x+dx[i]<5 and 0<= y+dy[i]<5:
                if p[x+dx[i]][y+dy[i]] == "P":
                    if p[x+dx[i]][y] == "O" or p[x][y+dy[i]]=="O":
                        return False
        dx,dy=[-2,0,2,0],[0,-2,0,2]
        mx,my = [1,0,-1,0],[0,1,0,-1]
        for i in range(4):
            if 0<=x+dx[i]<5 and 0<= y+dy[i]<5:
                if p[x+dx[i]][y+dy[i]] == "P":
                    if p[x+dx[i]+mx[i]][y+dy[i]+my[i]] == "O":
                        return False
        return True
    result=[]
    for p in places:
        flag=1
        for i in range(5):
            for j in range(5):
                if p[i][j]=="P":
                    if check(i,j) ==False:
                        flag=0
        if flag==1:
            result.append(1)
        else:
            result.append(0)
    return (result)
        
        