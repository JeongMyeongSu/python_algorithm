N = int(input())
arr = [list(input()) for _ in range(N)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
answer=[]
dange_sum=0
for i in range(N):
    for j in range(N):
        dange = 0
        house = 0
        if arr[i][j] == '1':
            q = [(i,j)]
            dange += 1
            house = 1
            while q:
                t = q.pop()
                arr[t[0]][t[1]] = 0
                for k in range(4):
                    if 0<= t[0]+dx[k] < N and 0 <= t[1]+dy[k] < N:
                        if arr[t[0]+dx[k]][t[1]+dy[k]] == '1':
                            q.append((t[0]+dx[k],t[1]+dy[k]))
                            arr[t[0]+dx[k]][t[1]+dy[k]] = 0
                            house += 1
        if house:
            answer.append(house)
            dange_sum += 1
print(dange_sum)
answer.sort()
for i in answer:
    print(i)
