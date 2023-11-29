t = int(input())
for _ in range(t):
    n = int(input())
    coins = [0]+list(map(int,input().split()))
    m = int(input())
    if min(coins[1:]) > m :
        print(0)
        continue
    # dp[i][j] j번째 동전을 사용했을때 i원이 만들어지는 경우의수

    dp =[[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1,n+1):
        if coins[i] > m:
            continue
        dp[coins[i]][i] = 1

    for i in range(coins[1]+1,m+1):

        for j in range(1,n+1):
            for k in range(1,n+1):
                if coins[j] <= coins[k] and i-coins[j] >=0:
                    
                    dp[i][j] += dp[i - coins[j]][k]

    ans = 0
    for i in dp[-1]:
        ans += i
    print(ans)