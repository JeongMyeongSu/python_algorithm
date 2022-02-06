import sys
input = sys.stdin.readline

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x
def union(x,y):
    p[find_set(x)]=find_set(y)

N,M,K = map(int,input().split())
edge_sets = []
for i in range(1,M+1):
    n1,n2 = map(int,input().split())
    edge_sets.append([i,n1,n2])
flag = True
for k in range(K):
    if flag:
        edge_set = edge_sets[k:]
        cnt = 0
        idx = 0
        answer = 0
        p = list(range(N+1))
        while cnt<N and idx<M-k:
            n1 = edge_set[idx][1]
            n2 = edge_set[idx][2]
            if find_set(n1) != find_set(n2):
                union(n1,n2)
                answer += edge_set[idx][0]
                cnt += 1
            idx += 1
        if cnt == N-1:
            print(answer,end=' ')
        else:
            print(0,end=' ')
            flag=0
    else:
        print(0,end=' ')