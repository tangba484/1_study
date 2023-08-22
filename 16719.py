
s = input()

result = [s]
flag = 0
def back(s):
    global flag
    k = len(s)
    if s == '':
        flag = 1
        return result
    for i in range(k):
        if i == k-1:
            S = s[:i]
        else:
            S = s[:i] + s[i+1:]
        if s > S:
            result.append(S)
            back(S)
            if flag == 1:
                return
            result.pop()

A = back(s)
result.sort()
for i in result:
    if i != '':
        print(i)
