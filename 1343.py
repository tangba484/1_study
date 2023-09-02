s = input()
n = len(s)
ans = list(s[:])
c = 0

for i in range(n):
    if s[i] == "X":
        c += 1
    
    if c == 2:
        ans[i] = "B"
        ans[i-1] = "B"
        c=0
c=0
for i in range(n):
    if ans[i] == "B":
        c += 1
    elif ans[i] == ".":
        c= 0
    
    if c == 4:
        ans[i] = "A"
        ans[i-1] = "A"
        ans[i-2] = "A"
        ans[i-3] = "A"
        c=0

if "X" in ans:
    print(-1)
else:
    for i in ans:
        print(i,end="")