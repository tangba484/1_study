s = input()
ans = {}
n = len(s)
for i in range(1,n+1):
    for j in range(n-i+1):
        ans[s[j:j+i]] = 1
print(len(ans))