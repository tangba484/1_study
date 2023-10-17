import sys
n,m = map(int,input().split())
L =[ int(sys.stdin.readline()) for _ in range(n)]
L.sort()
answer =[]

left,right = 0,0

while left<=right<n:
    dif = L[right] - L[left]
    if dif >=m:
        answer.append(dif)
        left += 1
    else:
        right += 1
        if right == n:
            break
print(min(answer))