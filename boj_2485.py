import sys
input = sys.stdin.readline
n = int(input())
l = [int(input()) for _ in range(n)]
l.sort()
diff=[]
for i in range(1,n):
    diff.append(l[i]-l[i-1])

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
x = diff[0]

for y in diff:
    x = gcd(x,y)
print((l[-1] - l[0])//x -n + 1)