# from sys import stdin
# N = int(input())
# par = list(map(int,stdin.readline().split()))
# left = [0]*(N+2)
# right = [0]*(N+2)
# C = int(input())
# par[C] = -1
# cnt = 0
# for i in range(N):
#     # if par[i] != -1:
#     if left[par[i]]:
#         right[par[i]] = i
#     else:
#         left[par[i]] = i
# def tree(n):
#     global cnt
#     if n:
#         if left[n] or right[n]:
#             tree(left[n])
#             tree(right[n])
#         else:
#             cnt += 1
# tree(1)
# print(left)
# print(right)
# print(cnt)

from sys import stdin
N = int(input())
par = list(map(int,stdin.readline().split()))
C = int(input())

adj_list = [[] for _ in range(N)]
for i in range(N):
    if par[i] == -1 or i==C:
        continue
    adj_list[par[i]].append(i)

visited = [0]*N
stack = [C]
while stack:
    t = stack.pop()
    visited[t] = 1
    for i in adj_list[t]:
        stack.append(i)
cnt = 0
for i in range(N):
    if not adj_list[i] and not visited[i]:
        cnt += 1
print(cnt)