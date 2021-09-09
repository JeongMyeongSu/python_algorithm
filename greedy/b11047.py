N,K = map(int,input().split())
change=[0]*N
count = 0
for n in range(N):
    change[n]=int(input())
for m in change[::-1]:
    count += K//m
    K %= m
print(count)