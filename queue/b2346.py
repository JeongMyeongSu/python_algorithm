import sys
from collections import deque
N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
seat = list(range(1,N))                                    # 자리 기억
now = 0                                # 현재 위치
temp = numbers.pop(now)
print(1,end=' ')
while seat:
    if temp>0:
        now = (now+temp-1)%len(seat)
    else:
        now = (now+temp)%len(seat)
    temp = numbers.pop(now)
    print(seat.pop(now)+1,end=" ")
    
