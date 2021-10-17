import sys
from collections import deque
M, N = map(int,sys.stdin.readline().split())
arr=[]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
welldone = deque()
for i in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        if row[j]==1:
            welldone.append((i,j))
    arr.append(row)
while welldone:
    t = welldone.popleft()
    for i in range(4):
        di = t[0]+dx[i]
        dj = t[1]+dy[i]
        if 0<=di<N and 0<=dj<M:
            if arr[di][dj] == 0:
                arr[di][dj] = arr[t[0]][t[1]]+1
                welldone.append((di,dj))
max_num = 0
flag = 0
for i in range(N):
    max_num = max(max_num,max(arr[i]))
    for j in range(M):
        if arr[i][j]==0:
            print(-1)
            flag = 1
            break
    if flag:
        break
if not flag:
    print(max_num-1)

