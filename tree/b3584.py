T = int(input())
for _ in range(T):
    N = int(input())
    adj_list = [[] for _ in range(N+1)]
    for __ in range(N-1):
        p,c = map(int,input().split())
        adj_list[c].append(p) # 거꾸로 넣음
    node1,node2 = map(int,input().split())
    visited1 = [0]*(N+1)
    visited2 = [0]*(N+1)
    q1 = [node1]
    q2 = [node2]
    while 1:
        if q1:
            t1 = q1[-1]
        if q2:
            t2 = q2[-1]
        visited1[t1] = 1
        visited2[t2] = 1
        for i in adj_list[t1]:
            q1.append(i)
        for i in adj_list[t2]:
            q2.append(i)
        if visited1[t1] and visited2[t1]:
            answer = t1
            break
        if visited1[t2] and visited2[t2]:
            answer = t2
            break
    print(answer)