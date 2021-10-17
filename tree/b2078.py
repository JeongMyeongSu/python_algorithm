# import sys
# (x,y) = list(map(int,input().split()))
# ans = 0
# li =[0]*100000000
# def tree(n,a,b,left,right):
#     li[n] = (a,b)
#     if a>x:
#         return
#     if b>y:
#         return
#     if (a,b) == (x,y):
#         print(left,right)
#         sys.exit()
#     else:
#         tree(2*n,a+b,b,left+1,right)
#         tree(2*n+1,a,a+b,left,right+1)
# tree(1,1,1,0,0)

(x,y) = list(map(int,input().split()))
left = right = 0
while 1:
    if x>y:
        left += 1
        x -= y
    else:
        right += 1
        y -= x
    if x == 1 and y == 1:
        break
print(left,right)