n , l = map(int,input().split())
now = 0
t = 0
for _ in range(n):
    d, r, g = map(int,input().split())
    t += d-now
    now = d
    if t % (r+g) <= r :
        t += r - t % (r+g)
t += l-now
print(t)