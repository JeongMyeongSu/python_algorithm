from sys import stdin

N, W = map(int,stdin.readline().split())
adj_list=[[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,stdin.readline().split())
    if u>v:
        u,v = v,u
    adj_list[u].append(v)
    adj_list[v].append(u)
q = [1]
visited = [0]*(N+1)
visited[1] = 1
cnt = 0
while q:
    t = q.pop()
    if len(adj_list[t])==1 and not visited[t]:
        cnt += 1
    visited[t] = 1
    for i in adj_list[t]:
        if not visited[i]:
            q.append(i)
if cnt:
    print(round(W/cnt,10))
else:
    print(W)