import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())
adj_arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1,n2,dist = map(int,input().split())
    adj_arr[n1].append((n2,dist))
    adj_arr[n2].append((n1,dist))
# for i in adj_arr:
#     print(*i)
distance = [0]*(n+1)
def DFS(x,visit,dist=0):
    for i,r in adj_arr[x]:
        if not visit[i]:
            visit[i]=True
            distance[i]=dist+r
            DFS(i,visit,dist+r)
            visit[i]=False
visit = [False]*(n+1)
visit[1]=True
DFS(1,visit)
max_node=distance.index(max(distance))
visit = [False]*(n+1)
visit[max_node]=True
DFS(max_node,visit)
print(max(distance))