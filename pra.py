a,b = map(int,input().split())
A=set()
B = set()

al = map(int,input().split())
bl = map(int,input().split())

for i in al:
    A.add(i)
for i in bl:
    B.add(i)
print(len(A-B)+len(B-A))