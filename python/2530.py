h,m,s = map(int, input().split())
x = int(input())
s = s + x
m = m+int(s/60)
h = h+int(m/60)
h = h%24
m = m%60
s = s%60
print("%s %s %s" %(h,m,s))