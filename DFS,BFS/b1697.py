import sys
from collections import deque
sys.setrecursionlimit(10**7)
N,K = map(int,sys.stdin.readline().split())
MAX = 100000
dist = [0]*(MAX+1)
Q = deque()
Q.append(N)
while dist:
    t = Q.popleft()
    if t == K:
        print(dist[K])
        break
    for x in [t-1,t+1,t*2]:
        if 0<x<=MAX and not dist[x]:
            dist[x] = dist[t]+1
            Q.append(x)