import sys
import math

N = int(sys.stdin.readline())
adj = [0 for _ in range(N+1)]
edges = []
for _ in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    edges.append((a,b))
    adj[a]+=1
    adj[b]+=1
D = 0
G = 0
for a,b in edges:
    D += (adj[a]-1)*(adj[b]-1)
for i in range(1,N+1):
    length = adj[i]
    if length>=3:
        G += length*(length-1)*(length-2) // 6
if D == 3*G:
    print('DUDUDUNGA')
elif D > 3*G:
    print('D')
else:
    print('G')