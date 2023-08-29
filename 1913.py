n = int(input()) 
Find = int(input())
arr = [ [0 for _ in range(n)] for _ in range(n) ]

dy =[0,1,0,-1]
dx =[1,0,-1,0]
x ,y = 0,0
num = n * n -1
arr[x][y] = n * n


while True:    
    for i in range(4):   
      while True :
        x = x + dx[i]
        y = y + dy[i]
        if x >= n or y >= n or x <  0 or y < 0 or arr[x][y] != 0 :
            x -= dx[i]
            y -= dy[i]         
            break
        else:           
            arr[x][y] = num
            if arr[x][y] == Find:
                ans1, ans2 = x,y
            num -= 1          
    if x == n//2 and y == n//2:
        break


for i in arr:
    print(*i)
print(ans1+1,ans2+1)