def prim(start,N):
    MST = [INF]*N
    V = (N+1)*N//2
    MST[start]=0
    visit = [False]*N
    cost = 0
    for i in range(N):
        minV = INF
        minVertex = -1
        for j in range(N):
            if not visit[j] and minV>MST[j]:
                minV = MST[j]
                minVertex = j
        visit[minVertex] = True
        cost += minV**(1/2)

        for j in range(N):
            if not visit[j] and MST[j]>dists[minVertex][j]:
                MST[j] = dists[minVertex][j]
    return cost

N = int(input())
stars = []
INF = 987654321
dists = [[INF]*N for _ in range(N)]
for i in range(N):
    stars.append([i]+list(map(float,input().split())))
for i in range(N):
    for j in range(i+1,N):
        dist = (stars[i][1]-stars[j][1])**2+(stars[i][2]-stars[j][2])**2
        dists[i][j] = dist
        dists[j][i] = dist

print('{:.2f}'.format(prim(0,N)))

