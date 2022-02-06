# 실패했지만 다시 풀기가 너무 귀찮.
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
link = {}
numbers=[]
def bfs(n):
    global max_case
    q=deque([n])
    cnt = 0
    while q:
        t=q.popleft()
        cnt += 1
        if t in link:
            for i in link[t]:
                q.append(i)
    return cnt
for _ in range(M):
    a,b = map(int,input().split())
    if b in link:
        link[b].append(a)
    else:
        link[b]=[a]
    if b not in numbers:
        numbers.append(b)
max_case = 0
answer = []
for j in numbers:
    k=bfs(j)
    if max_case<k:
        answer=[j]
        max_case = k
    elif max_case==k:
        answer.append(j)
print(*sorted(answer))
