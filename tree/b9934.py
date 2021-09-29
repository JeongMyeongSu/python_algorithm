from sys import stdin

K = int(input())
num = stdin.readline().split()
N = 2**K
answer = [0]*N
cnt = 0
def tree(n):
    global cnt
    if n < N:
        tree(2*n)
        answer[n]=num[cnt]
        cnt += 1
        tree(2*n+1)
tree(1)
s=1
e=2
while s<N:
    for i in range(s,e):
        print(answer[i],end=" ")
    print()
    s *= 2
    e *= 2




