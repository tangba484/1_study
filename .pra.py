import sys
sys.setrecursionlimit(10**5)

n,r,c = map(int,input().split())

def R(n,r,c):
    if n == 1:
        return 2*r + c
    l = 2**n
    half = l/2
    if r < half and c < half :
        ans =  R(n-1,r,c)
    if r<half and c >= half:
        ans =  half*half+R(n-1,r,c-half)
    if r>=half and c < half:
        ans =  half*half*2 + R(n-1,r-half,c)
    if r>=half and c >= half:
        ans = 3*half*half + R(n-1,r-half,c-half)
    return ans

print(int(R(n,r,c)))