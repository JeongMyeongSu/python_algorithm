# N = int(input())

# Hanoi = [list(map(int, input().split())), [], []]

# target = N
# i = 0
# cnt = 0

# log = []

# while len(Hanoi[2]) < N:
#     i %= 2
#     if target in Hanoi[i]:
#         while True:
#             t = Hanoi[i].pop()
#             cnt += 1
#             if t == target:
#                 Hanoi[2].append(t)
#                 log.append(f"{i + 1} {3}")
#                 target -= 1
#                 break
#             else:
#                 Hanoi[not i].append(t)
#                 log.append(f"{i + 1} {(not i) + 1}")
#     i += 1

# print(cnt)
# for l in log:
#     print(l)
def lining8(n,A):
    global cnt
    if n==8:
        cnt += 1
        return
    for i in range(1,9):
        if not A:
            lining8(n+1,[i])
        if A and adj[A[-1]][i] and i not in A :
            lining8(n+1,A+[i])
adj = [[1]*9 for _ in range(9)]
N = int(input())
cnt = 0
for _ in range(N):
    a,b = map(int,input().split())
    adj[a][b]=0
    adj[b][a]=0
lining8(0,[])
print(cnt)

