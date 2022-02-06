N = int(input())
A = [[0]*N for _ in range(N)]
for i in range(N):
    coins = input()
    for j in range(N):
        if coins[j]=='T':
            A[i][j] = 1

