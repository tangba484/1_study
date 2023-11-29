s = input()
D={}

for i in s:
    if i in D:
        D[i] += 1
    else:
        D[i] = 1

K = sorted(D.keys())

a =""
cnt = 0

for i in K:
    if D[i] % 2 == 1:
        cnt += 1
        a += i

if cnt >= 2:
    print("I'm Sorry Hansoo")
else:
    answer =""
    for i in K:
        answer += i*(D[i]//2)
    print(answer + a + answer[::-1])