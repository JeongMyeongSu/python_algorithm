N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
same = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '-':
            if 0 <= j-1 and arr[i][j-1] == '-':
                same += 1
            if j+1 < M and arr[i][j+1] == '-':
                same += 1
        if arr[i][j] == '|':
            if 0 <= i-1 and arr[i-1][j] == '|':
                same += 1
            if i+1 < N and arr[i+1][j] == '|':
                same += 1
print(M*N-same//2)