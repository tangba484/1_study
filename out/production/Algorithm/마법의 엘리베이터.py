from collections import deque
def solution(n):
    a = [0]+list(map(int,str(n)))
    cnt = 0
    c = 0
    for k in range(len(a)-1):
        i = a[-k-1]
        if c == 1:
            i += 1
        c = 0
        if i <= 4:
            cnt += i
            c = 0
        elif i ==5:
            if a[-k-2]<5:
                cnt += i
                c=0
            else:
                cnt += i
                c=1
        elif i > 5:
            cnt += 10 -i
            c = 1
    if c == 1:
        return (cnt + 1)
    else:
        return (cnt)