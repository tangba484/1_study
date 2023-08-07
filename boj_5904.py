n = int(input())

ans=""
def s(k):
    global ans
    if k ==0:
        return 3
    a = s(k-1)
    return a + k+3 + a

k=0
dp=[0]
while 1:
    R = s(k)
    dp.append(R)
    if n<=R:
        break
    k += 1

def sol(n,k):
    if dp[k]+ 1<=n <= dp[k+1]-dp[k]:
        if dp[k] + 1 ==n:
            return "m"
        else:
            return "o"
    if n > dp[k+1]-dp[k]:
        n = n -(k+3) - dp[k]
        k -= 1
        return sol(n,k)
    else:
        k -= 1
        return sol(n,k)
print(sol(n,k))
    