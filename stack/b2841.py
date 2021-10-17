from sys import stdin
N,P = map(int,stdin.readline().split())
stack = [[] for _ in range(N+1)]
ans = 0
for _ in range(N):
    n, p = map(int,stdin.readline().split())
    if stack[n] and stack[n][-1] > p:
        while stack[n] and stack[n][-1]>p:
            ans += 1
            stack[n].pop()
        if stack[n] and stack[n][-1]==p:
            continue
        else:
            stack[n].append(p)
            ans += 1
    elif stack[n] and stack[n][-1] == p:
        continue
    else:
        stack[n].append(p)
        ans += 1
print(ans)
    
