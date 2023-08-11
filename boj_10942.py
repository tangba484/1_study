import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int,input().split()))
ans = [[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    ans[i][i] = 1

for i in range(2,n):
    for s in range(n - i + 1):
        e = s + i - 1
        if l[s]==l[e] and ans[s+1][e-1] == 1:
            ans[s][e] = 1

m = int(input())
for _ in range(m):
    s,e = map(int,input().split())
    print(ans[s-1][e-1])