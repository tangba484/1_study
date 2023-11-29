import sys
n = int(input())
D = {}

for _ in range(n):
    name , state = sys.stdin.readline().split()
    
    if state == "enter" :
        D[name] = 1
    else:
        D[name] = 0
answer =[]
for x,y in D.items():
    if y == 1:
        answer.append(x)
answer.sort(reverse=True)
for i in answer:
    print(i)