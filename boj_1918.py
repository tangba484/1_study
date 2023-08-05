s = list(input())
stack = []
ans =""
for i in s:
    if "A"<=i<="Z":
        ans += i
    elif i in ["*","/"]:
        while stack and stack[-1]!="("and stack[-1] in ["*","/"]:
            ans += stack.pop()
        stack.append(i)
    elif i in ["+","-"]:
        while stack and stack[-1] !="(":
            ans += stack.pop()
        stack.append(i)
    elif i =="(":
        stack.append(i)
    elif i ==")":
        while stack and stack[-1] !="(":
            ans += stack.pop()
        stack.pop()
while stack:
    ans += stack.pop()
print(ans)