import sys
sys.setrecursionlimit(10000)
from sys import stdin
from collections import deque

N = int(stdin.readline())
arr = [stdin.readline() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
# def dfs(i,j):
#     visited[i][j] = 1
#     for k in range(4):
#         di = i+dx[k]
#         dj = j+dy[k]
#         if 0<=di<N and 0<=dj<N and not visited[di][dj]:
#             if arr[i][j]==arr[di][dj]:
#                 dfs(di,dj)
def bfs(i,j):
    visited[i][j] = 1
    q = deque((i,j))
    while q:
        t = q.popleft()
        ti = t[0]
        tj = t[1]
        for k in range(4):
            di = ti+dx[k]
            dj = tj+dy[k]
            if 0<=di<N and 0<=dj<N and not visited[di][dj]:
                if arr[ti][tj]==arr[di][dj]:
                    visited[di][dj]=1
                    q.append((di,dj))
def bfs2(i,j):
    visited[i][j] = 1
    q = deque((i,j))
    while q:
        t = q.popleft()
        ti = t[0]
        tj = t[1]
        for k in range(4):
            di = ti+dx[k]
            dj = tj+dy[k]
            if 0<=di<N and 0<=dj<N and not visited2[di][dj]:
                if arr[ti][tj]==arr[di][dj]:
                    visited2[di][dj]=1
                    q.append((di,dj))
                elif arr[ti][tj]=='R'and arr[di][dj]=='G':
                    q.append((di,dj))
                elif arr[ti][tj]=='G'and arr[di][dj]=='R':
                    q.append((di,dj))
# def dfs2(i,j):
#     visited2[i][j] = 1
#     for k in range(4):
#         di = i+dx[k]
#         dj = j+dy[k]
#         if 0<=di<N and 0<=dj<N and not visited2[di][dj]:
#             if arr[i][j]==arr[di][dj]:
#                 dfs2(di,dj)
#             elif arr[i][j]=='R'and arr[di][dj]=='G':
#                 dfs2(di,dj)
#             elif arr[i][j]=='G'and arr[di][dj]=='R':
#                 dfs2(di,dj)


area = area2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            area += 1
        if not visited2[i][j]:
            bfs2(i,j)
            area2 += 1
print(area,area2)