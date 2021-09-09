from collections import deque
N = int(input())
li = deque(range(1,N+1))
while len(li)>1:
    li.popleft()
    li.rotate(-1)
print(li[0])
