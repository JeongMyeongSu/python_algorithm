from sys import stdin
N,Q = map(int,stdin.readline().split())
area = [0]*(N+1)
for i in range(Q):
    my_area = a = int(stdin.readline())
    flag = 1
    while a>0:
        if area[a] !=0:
            flag=0
            answer = a
        a //= 2
    if flag:
        answer = 0
        area[my_area] = 1
    print(answer)