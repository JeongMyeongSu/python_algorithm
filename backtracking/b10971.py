import sys
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [0]*N
min_cost = 1000000
def backtracking(now,cost,visit,cnt):
    global min_cost
    if cost>min_cost:
        return
    if cnt<N:
        for i in range(N):
            if visit[i]==0 and arr[now][i]:
                visit[i]=1
                backtracking(i,cost+arr[now][i],visit,cnt+1)
                visit[i]=0
    else:
        cost += arr[now][j]
        if cost<min_cost:
            min_cost = cost
for j in range(N):
    backtracking(j,0,visited,0)
print(min_cost) if min_cost != 1000000 else print(0)
