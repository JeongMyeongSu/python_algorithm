import sys
from collections import deque
N = int(sys.stdin.readline())
adj = [[] for _ in range(N+1)]
visit = [0]*(N+1)
for _ in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
q= deque()
q.append(1)
ans = 0
visit[1]=1
while q:
    t = q.popleft()
    x = len(q)
    for i in adj[t]:
        if not visit[i]:
            q.append(i)
            visit[i] = visit[t]+1
    if x == len(q):
        ans += visit[t]-1
if ans%2:
    print('Yes')
else:
    print('No')

