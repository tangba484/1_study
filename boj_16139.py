import sys
s = input()
input = sys.stdin.readline
ls = len(s)
X ="abcdefghijklmnopqrstuvwxyz"
D={}
for i in X:
    D[i] = [0]*ls
D[s[0]][0] = 1
for i in range(1,ls):
    x = s[i]

    D[x][i] = D[x][i-1] + 1
    for j in X:
        if x!=j:
            D[j][i] = D[j][i-1]

t = int(input())

for _ in range(t):
    S,left,right = input().split()
    left,right = int(left),int(right)
    if left == right:
        if S == s[left]:
            print(1)
        else:
            print(0)
    elif left == 0:
        print(D[S][right])
    else:
        print(D[S][right] - D[S][left-1])