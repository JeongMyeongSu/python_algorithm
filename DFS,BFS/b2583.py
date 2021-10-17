M,N,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(K)]
all = [[1]*N for _ in range(M)]

for square in arr:
    for i in range(square[1],square[3]):
        for j in range(square[0],square[2]):
            all[i][j] = 0

dx=[0,0,1,-1]
dy=[1,-1,0,0]
answer=[]
for i in range(M):
    for j in range(N):
        counter=0
        if all[i][j] == 1:
            q=[(i,j)]
            counter = 1
            all[i][j] = 0
            while q:
                t = q.pop()
                for k in range(4):
                    if 0 <= t[0]+dx[k] <M and 0 <= t[1]+dy[k] < N:
                        if all[t[0]+dx[k]][t[1]+dy[k]] == 1:
                            q.append((t[0]+dx[k],t[1]+dy[k]))
                            all[t[0]+dx[k]][t[1]+dy[k]] = 0
                            counter += 1
            answer.append(counter)
print(len(answer))
print(*sorted(answer))
