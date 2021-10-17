import sys
sys.setrecursionlimit(100000)
dx = [0,0,1,1,1,-1,-1,-1]
dy = [1,-1,1,0,-1,1,0,-1]
def island(i,j):
    for x in range(8):
        di = i+dx[x]
        dj = j+dy[x]
        if 0<=di<M and 0<=dj<N and arr[di][dj]==1:
            arr[di][dj] = 0
            island(di,dj)

while 1:
    answer = 0
    N,M = map(int,sys.stdin.readline().split())
    if not N and not M:
        break
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if arr[i][j]==1:
                island(i,j)
                answer += 1
    print(answer)