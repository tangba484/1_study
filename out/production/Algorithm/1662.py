s = list((input()))
k = len(s)
for i in range(k-1):
    if s[i].isdigit() and s[i+1] !="(":
        s[i] = 1
    elif s[i].isdigit() and s[i+1] == "(":
        s[i] = int(s[i])
if s[k-1].isdigit():
    s[k-1] = 1

def R(s):
    k = len(s)
    b = 0

    for i in range(k):
        if s[i] == "(":
            start = i
        elif s[i] == ")":
            end = i
            b = 1
            break
    if b == 0:
        return sum(s)
    else:
        S = sum(s[start+1:end])*(s[start - 1])
        s = s[0:start - 1] +[S] + s[end + 1:]
        return R(s)

print(R(s))