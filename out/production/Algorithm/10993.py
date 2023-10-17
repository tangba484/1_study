n = int(input())

def R(n):
    if n == 1:
        return ["*"]
    elif n == 2:
        return ["*****","***","*"]
    A = R(n-1)
    h = 2*len(A) + 1
    if n %2 == 0:
        w = 2*len(A[-1]) + 3
        s=["*"]
        for i in range(1,len(A)):
            s.append("*" + (2*i - 1)*" " + "*")
        for i in range(len(A)):
            s.append("*" + " "*2*i + A[-i-1] + " "*2*i + "*")
        s.append("*"*w)
        return s[::-1]
    elif n % 2 == 1:
        w = 2*len(A[0]) + 3
        s=["*"]
        for i in range(1,len(A)):
            s.append("*" + (2*i - 1)*" " + "*")
        for i in range(len(A)):
            s.append("*"+" "*(2*i)+A[i] + " "*(2*i) + "*")
        s.append("*"*w)
        return s

A = R(n)

k = len(A)


if n%2 == 1:
    s=[]
    for i in range(k):
        s.append(" "*i+A[-i-1])
    for i in s[::-1]:
        print(i)
else:
    for i in range(k):
        print(" "*i + A[i])