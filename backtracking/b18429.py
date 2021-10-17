import sys
N,K = map(int,sys.stdin.readline().split())
machine = list(map(int,sys.stdin.readline().split()))
cnt = 0
visited = [0]*(N+1)
def backtracking(n,weight):
    global cnt
    if weight<500:
        return
    if n == N:
        cnt += 1
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            backtracking(n+1,weight+machine[i]-K)
            visited[i] = 0
backtracking(0,500)
print(cnt)
    
    