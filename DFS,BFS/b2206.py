import sys # 다 되는데 메모리 초과
sys.setrecursionlimit(1000000)
N,M = map(int,sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
flag = 0
min_depth = 100000
def BFS(i,j):
    global flag,min_depth
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1
    stack = []
    stack.append((i,j))
    while stack:
        i,j = stack[0]
        del stack[0]
        if i == N-1 and j == M-1:
            flag = 1
            min_depth = min(min_depth,visited[i][j])
            return
        for x in range(4):
            di = i+dx[x]
            dj = j+dy[x]
            if 0<=di<N and 0<=dj<M and arr[di][dj]=='0' and not visited[di][dj]:
                stack.append((di,dj))
                visited[di][dj] = visited[i][j]+1

for k in range(N):
    for l in range(M):
        if arr[k][l]=='1':
            if (1<=k<N-1 and arr[k-1][l]=='0' and arr[k+1][l]=='0') or (1<=l<M-1 and arr[k][l-1]=='0' and arr[k][l+1]=='0'):
                arr[k][l]='0'
                BFS(0,0)
                arr[k][l]='1'
        else:
            BFS(0,0)
if flag:
    print(min_depth)
else:
    print(-1)
    