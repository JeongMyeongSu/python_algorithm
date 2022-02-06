import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j]=0
            shark = (i,j)
shark_size = 2
dx=[-1,0,0,1] # 위쪽, 왼쪽 먼저
dy=[0,-1,1,0]
eat = 0
time = 0
def find_fish(a,b):
    global eat,shark_size,time
    global shark
    q = deque()
    q.append([a,b,0])
    visited=[[0]*N for _ in range(N)]
    new_q = []
    flag = 1e9
    while q:
        r,c,dist = q.popleft()
        limit=99
        if dist>limit:
            break
        visited[r][c]=1
        if dist > flag:
            break
        for x in range(4):
            dr = r+dx[x]
            dc = c+dy[x]
            if 0<=dr<N and 0<=dc<N and not visited[dr][dc]:
                if arr[dr][dc]==0 or arr[dr][dc]==shark_size:
                    q.append([dr,dc,dist+1])
                elif arr[dr][dc]<shark_size:                    
                    new_q.append((dr,dc,dist+1))
                    flag = dist
                    limit=dist+1
    if new_q:
        new_q=sorted(new_q,key=lambda x:(x[2],x[0],x[1]))
        eat += 1
        dr,dc,dist = new_q[0]
        shark = (dr,dc)
        time += dist
        arr[a][b]=0
        new_q = []                       
        if eat>=shark_size:
            eat=0
            shark_size += 1
        return 1
    return 0
while 1:
    if find_fish(shark[0],shark[1]):
        continue
    else:
        break
print(time)
