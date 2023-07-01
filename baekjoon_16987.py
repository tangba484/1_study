n = int(input())
s,w=[],[]
for _ in range(n):
    x,y =(map(int,input().split()))
    s.append(x)
    w.append(y)
answer =[]
def back(now,s,w,cnt):
    if now == n:
        return answer.append(cnt)
    if s[now] <=0:
        back(now+1,s,w,cnt)
    else:
        flag = 0
        for i in range(n):
            if i == now:
                continue
            elif s[i] > 0:
                flag = 1
                s[now] -= w[i]
                s[i] -= w[now]
                if s[now] <=0:
                    cnt +=1
                if s[i] <=0:
                    cnt +=1
                back(now+1,s,w,cnt)
                if s[now] <=0:
                    cnt -=1
                if s[i] <=0:
                    cnt -=1          
                s[now] += w[i]
                s[i] += w[now]
        if flag == 0:
            back(n,s,w,cnt) 

back(0,s,w,0)

print(max(answer))