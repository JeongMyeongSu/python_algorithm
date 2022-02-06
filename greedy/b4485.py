import sys
from heapq import heappush, heappop
def dijkstra():
    global min_fee
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = []
    heappush(q,[arr[0][0],0,0,0])
    visit = [[29999]*N for _ in range(N)]
    visit[0][0] = arr[0][0]
    while q:
        fee,i,j,cnt = heappop(q)
        if cnt > N**2:
            continue
        for x in range(4):
            di = i+dx[x]
            dj = j+dy[x]
            if 0<=di<N and 0<=dj<N:
                new_cost = arr[di][dj]+fee
                if visit[di][dj] > new_cost:
                    heappush(q,[new_cost,di,dj,cnt+1])
                    visit[di][dj] = new_cost
    return visit[N-1][N-1]
while 1:
    k = 1
    min_fee = 987654
    N = int(sys.stdin.readline())
    if N == 0:
        break
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    print('Problem {}: {}'.format(k,dijkstra()))
    k += 1