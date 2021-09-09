N,M = map(int,input().split())
snow = list(map(int,input().split()))
max_ball = 0
def dfs(counter,n,ball):
    global max_ball
    if n ==N-1 or counter == M:
        if max_ball < ball:
            max_ball = ball
    else:
        if n+1 < N:
            dfs(counter+1,n+1,ball+snow[n+1])
        if n+2 < N:
            dfs(counter+1,n+2,ball//2+snow[n+2])
    return max_ball
print(dfs(0,-1,1))
