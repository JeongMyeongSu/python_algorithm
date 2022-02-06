from collections import deque
dx=[1,1,-1,-1,2,2,-2,-2]
dy=[2,-2,2,-2,1,-1,1,-1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    q = deque()
    q.append([start[0],start[1],0])
    visit = [[False]*N for _ in range(N)]
    visit[start[0]][start[1]] = True
    flag = 0
    while q:
        i,j,cnt = q.popleft()
        for x in range(8):
            di = i+dx[x]
            dj = j+dy[x]
            if 0<=di<N and 0<=dj<N and not visit[di][dj]:
                q.append([di,dj,cnt+1])
                visit[di][dj]=True
                if [di,dj]==end:
                    print(cnt+1)
                    flag = 1
                    break
        if flag:
            break
    if not flag:
        print(0)

