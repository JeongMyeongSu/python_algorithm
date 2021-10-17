import sys
sys.stdin = open('input.txt')

sys.setrecursionlimit(1000000)
N,M = map(int,sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(N)]
dx = [0,0,1,-1] # 우 좌 하 상
dy = [1,-1,0,0]
flag = 0
min_depth = 1000000
visited = [[0]*M for _ in range(N)]
def dfs(i,j,depth,chance,visit):
    print(i,j)
    global flag,min_depth
    visit[i][j] = 1
    if depth>min_depth:
        return
    if i == N-1 and j == M-1:
        flag = 1
        if depth < min_depth:
            min_depth = depth
        return
    for x in range(4):
        di = i+dx[x]
        dj = j+dy[x]
        if 0<=di<N and 0<=dj<M and visit[di][dj]==0:
            if arr[di][dj]=='0':
                dfs(di,dj,depth+1,chance,visit)
            if arr[di][dj]=='1' and chance == 0:
                dfs(di,dj,depth+1,1,visit)
dfs(0,0,1,0,visited)

if flag:
    print(min_depth)
else:
    print(-1)
 