R, C, K = map(int,input().split())
arr = [list(input()) for _ in range(R)]
print(arr)
cnt = 0
visit = [[0]*C for _ in range(R)]
visit[0][C-1] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def backtracking(i,j,n,visit):
    global cnt
    # print(i,j,n,cnt)
    if arr[i][j] == 'T':
        return
    elif (i,j) == (R-1,0) and n==K:
        cnt += 1
        return
    for x in range(4):
        di = i+dx[x]
        dj = j+dy[x]
        if 0<=di<R and 0<=dj<C and visit[di][dj] == 0:
            visit[di][dj] = 1
            backtracking(di,dj,n+1,visit)
            visit[di][dj] = 0


backtracking(0,C-1,1,visit)
print(cnt)