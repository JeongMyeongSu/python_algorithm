def DFS(n):
    print(n,end=" ")
    visit[n] = True
    for i in sorted(adj_list[n]):
        if not visit[i]:
            DFS(i)

def BFS(n):
    q = [n]
    visit[n] = True
    while q:
        t = q.pop(0)
        print(t,end=" ")
        for i in sorted(adj_list[t]):
            if not visit[i]:
                q.append(i)
                visit[i] = True

N,M,V = map(int,input().split())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    n1,n2 = map(int,input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)
visit = [True]+[False]*N
DFS(V)
print()
visit = [True]+[False]*N
BFS(V)
