import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())

def bugeffect(a,b):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for x in range(4):
        da = a+dx[x]
        db = b+dy[x]
        if 0<=da<M and 0<=db<N and bat[da][db]:
            bat[da][db]=0
            bugeffect(da,db)

for tc in range(1,T+1):
    M,N,K = map(int,sys.stdin.readline().split())
    bug = [list(map(int,sys.stdin.readline().split())) for _ in range(K)]
    bat = [[0]*N for _ in range(M)]
    for i,j in bug:
        bat[i][j] = 1
    cnt = 0
    for i in range(M):
        for j in range(N):
            if bat[i][j]:
                bugeffect(i,j)
                cnt += 1
    print(cnt)
