import sys
sys.setrecursionlimit(10 ** 6)
N = int(sys.stdin.readline())
adj_list=[[] for _ in range(N+1)]
parent = [0]*(N+1)
for _ in range(N-1):
    s,e = map(int,input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

def tree(p=1):
    for i in adj_list[p]:
        if not parent[i]:
            parent[i] = p
            tree(i)
tree()
for i in range(2,N+1):
    if parent[i]:
        print(parent[i])
