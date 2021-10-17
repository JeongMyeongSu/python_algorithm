import sys
from collections import deque
T = int(sys.stdin.readline())
for tc in range(T):
    N = int(sys.stdin.readline())
    left = list(map(int,sys.stdin.readline().split()))
    right = list(map(lambda x:int(x)-1000,sys.stdin.readline().split()))
    answer = 0
    for i in right:
        if i in left:
            answer += 1 
    print(answer//2)


