n = int(input())
l = list(map(int,input().split()))

stack = []
i = 0
ans = 1

while i < n-1:
    if l[i] > l[i+1]:
        i +=1
        continue
    if l[i] == l[i+1]:
        ans = max(ans,2)
        i += 1
        continue
    if l[i] < l[i+1]:
        cnt = 0
        stack = [l[i]]
        while i<n-1 and l[i]<l[i+1]:
            stack.append(l[i+1])
            i += 1
        if i<n-1 and stack.pop() == l[i+1]:
            cnt += 2
            i += 1
        else:
            cnt += 1
        while stack and i<n-1:
            if stack.pop() == l[i+1]:
                cnt += 2
                i += 1
            else:
                break
        ans = max(ans,cnt)
        
print(ans)