import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
queue = deque([(0,0)])
while queue:
    t = queue.popleft()
    for i in range(4):
        di = t[0]+dx[i]
        dj = t[1]+dy[i]
        if 0<=di<N and 0<=dj<M:
            if arr[di][dj]=='1':
                arr[di][dj]=arr[t[0]][t[1]]+'1'
                queue.append((di,dj))
print(len(arr[N-1][M-1]))
