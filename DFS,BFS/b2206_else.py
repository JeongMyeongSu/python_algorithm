import sys # 다 되는데 메모리 초과
N,M = map(int,sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def BFS(i,j):
    visited = [[[0]*2 for _ in range(M)] for __ in range(N)]
    visited[i][j][1] = 1
    queue = []
    queue.append((i,j,1))
    while queue:
        i,j,chance = queue.pop(0)
        if i == N-1 and j == M-1:
            return visited[i][j][chance]
        for x in range(4):
            di = i+dx[x]
            dj = j+dy[x]
            if 0<=di<N and 0<=dj<M and arr[di][dj]=='1' and chance:
                queue.append((di,dj,0))
                visited[di][dj][0] = visited[i][j][1]+1
            elif 0<=di<N and 0<=dj<M and arr[di][dj]=='0' and visited[di][dj][chance]==0:
                queue.append((di,dj,chance))
                visited[di][dj][chance] = visited[i][j][chance]+1
    return -1
print(BFS(0,0))



# from typing import Deque
# import sys
# input = sys.stdin.readline

# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# N, M = map(int, input().split())
# field = [list(map(int, input().rstrip("\n"))) for _ in range(N)]
# check = [[[N * M] * M for _ in range(N)] for _ in range(2)]

# if N == 1 and M == 1:
#     print(1)
#     exit()

# queue = Deque()
# queue.append((0, 0, 1, 1))

# while queue:
#     row, col, step, power = queue.popleft()
#     for to in range(0, 4):
#         y = row + dy[to]
#         x = col + dx[to]

#         if 0 <= y < N and 0 <= x < M:
#             if field[y][x] == 1 and power and check[0][y][x] > step + 1:
#                 check[0][y][x] = step + 1
#                 queue.append((y, x, step + 1, 0))

#             elif field[y][x] == 0:
#                 if check[power][y][x] > step + 1:
#                     check[power][y][x] = step + 1
#                     queue.append((y, x, step + 1, power))

#     if check[0][-1][-1] != N * M or check[1][-1][-1] != N * M:
#         print(min(check[0][-1][-1], check[1][-1][-1]))
#         break
# else:
#     print(-1)