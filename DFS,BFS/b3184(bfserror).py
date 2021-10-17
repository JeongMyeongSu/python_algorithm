from sys import stdin
R,C = map(int,stdin.readline().split())
arr = [stdin.readline() for _ in range(R)]
visited = [[0]*C for _ in range(R)]
areas = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(i,j):
    global wolf,sheep
    if visited[i][j]:
        return
    visited[i][j]=1
    if arr[i][j] == 'v':
        wolf += 1
    elif arr[i][j] == 'o':
        sheep += 1
    for k in range(4):
        di = i+dx[k]
        dj = j+dy[k]
        if 0<=di<R and 0<=dj<C and not visited[di][dj]:
            if arr[di][dj] == '#':
                continue
            else:
                dfs(di,dj)
        
for i in range(R):
    for j in range(C):
        if arr[i][j]=='o':
            areas.append((i,j))
        elif arr[i][j]=='v':
            areas.append((i,j))
total_sheep = 0
total_wolf = 0
for i,j in areas:
    sheep = 0
    wolf = 0
    dfs(i,j)
    print(i,j,sheep,wolf)
    if sheep>wolf:
        total_sheep += sheep
    else:
        total_wolf += wolf
print(total_sheep,total_wolf)