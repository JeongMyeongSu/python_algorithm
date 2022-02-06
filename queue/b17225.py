import sys
from collections import deque
A,B,N = map(int,sys.stdin.readline().split())
A_set = deque()
B_set = deque()
t1=t2=0
for _ in range(N):
    t,color,num = map(str,sys.stdin.readline().split())
    t = int(t)
    num = int(num)
    if color=='B':
        if t1>t:
            t=t1
        for i in range(num):# t t+A t+2A 
            A_set.append(t+i*A)
        t1 = t+A*i
    else:
        if t2>t:
            t=t2
        for i in range(num):
            B_set.append(t+i*A)
        t2 = t+B*i
order_set_A = deque()
order_set_B = deque()
i = 1
while A_set and B_set:
    if B_set[0]<A_set[0]:
        B_set.popleft()
        order_set_B.append(i)
    else:
        A_set.popleft()
        order_set_A.append(i)
    i += 1
while A_set:
    order_set_A.append(i)
    A_set.popleft()
    i += 1
while B_set:
    order_set_B.append(i)
    B_set.popleft()
    i += 1
print(len(order_set_A))
for x in order_set_A:
    print(x,end=' ')
print()
print(len(order_set_B))
for x in order_set_B:
    print(x,end=' ')
        