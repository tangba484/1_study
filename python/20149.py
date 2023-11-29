# x1,y1,x2,y2 = map(int,input().split())

# x3,y3,x4,y4 = map(int,input().split())
# if x3!=x4:
#     m = (y3-y4)/(x3-x4)
#     c1 = -m*x1 + y1
#     c2 = -m*x2 + y2
#     y_intercept= -m*x3 + y3
#     if min(c1,c2) <= y_intercept<=max(c1,c2):
#         print("YES")
#     else:
#         print("NO")
# elif x3 == x4:
#     if x1 != x2:
#         m = (y1-y2)/(x1-x2)
#         c1 = -m*x3 + y3
#         c2 = -m*x4 + y4
#         y_intercept= -m*x1 + y1
#         if min(c1,c2) <= y_intercept<=max(c1,c2):
#             print("YES")
#         else:
#             print("NO")
#     elif x1 == x2:
#         if x1!= x3:
#             print("NO")
#         else:
            