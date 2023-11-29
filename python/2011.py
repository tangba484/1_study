s = "0"+(input())
k = len(s) - 1

dp=[[0 for _ in range(k+1)]for _ in range(3)]

dp[1][1] = 1
dp[2][0] = 1
flag = 0
if s[1] == "0":
    flag = 1
for i in range(1,k+1):
    if s[i] == "0" and s[i-1]=="0":
        flag = 1
if flag == 1:
    print(0)
else:
    for i in range(2,k+1):
        for j in range(1,3):
            if j == 1:
                if s[i] == "0":
                    dp[j][i] = 0
                else:
                    dp[j][i] = dp[1][i-1]%1000000 + dp[2][i-1]%1000000
            elif j == 2:
                if 0<int(s[i-1])*10 + int(s[i]) <=26:
                    if s[i-1] == "0":
                        dp[j][i] = 0
                    else:
                        dp[j][i] = (dp[2][i-2] + dp[1][i-2])%1000000
                else:
                    dp[j][i] = 0
    print((dp[1][-1] + dp[2][-1])%1000000)