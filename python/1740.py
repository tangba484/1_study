n = bin(int(input()))[2:]

ans = 0

for i in range(len(n)-1,-1,-1):
    if n[-i-1] == "1":
        ans += 3** i
    
print(ans)