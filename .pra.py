graph = [[1 for _ in range(8)] for _ in range(6)]
graph[0][4] = 0
graph[-1][4] = 0

for i in range(2):
    for j in range(6,8):
        graph[i][j] = 0
        graph[-i-1][j] = 0
        
graph[0][1]= 2
graph[0][2]= 2
graph[1][2]= 2

graph[2][0] = 9
graph[3][0] = 9
graph[2][1] = 9
graph[3][1] = 9

graph[1][3]= 3
graph[2][2]= 3
graph[2][3]= 3

graph[4][2]= 4
graph[5][1]= 4
graph[5][2]= 4

graph[3][2]= 5
graph[3][3]= 5
graph[4][3]= 5

graph[4][4]= 6
graph[4][5]= 6
graph[5][5]= 6

graph[2][4] = 7
graph[3][4] = 7

graph[0][5] = 8
graph[1][5] = 8
graph[2][5] = 8

for i in graph:
    print(i)