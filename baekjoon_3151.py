n = int(input())
l = list(map(int,input().split()))
l.sort()

cnt = 0
for i in range(n-2):
    left = i+1
    right = n-1
    m = 99999
    while left<right:
        x = l[left]+l[right]+l[i]

        if x == 0:
            if l[left] == l[right]:
                cnt += right-left
            else:
                if m > right:
                    m = right
                    while m >=0 and l[right] == l[m-1]:
                        m -= 1
                cnt += right - m + 1
            left += 1

        elif x<0:
            left += 1
        else:
            right -= 1
print(cnt)
