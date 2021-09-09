N = int(input())
a,b = map(int,input().split())
E = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(E):
    n1,n2 = map(int,input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)
q = [a]
visited= [-1]*(N+1)
visited[a] = 0
while q:
    t = q.pop(0)
    for i in adj[t]:
        if visited[i] == -1:
            q.append(i)
            visited[i] = visited[t]+1
print(visited[b])

