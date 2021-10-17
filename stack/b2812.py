from sys import stdin

N, K = map(int,stdin.readline().split())
num = stdin.readline()
que = ''
cnt = 0
for i in range(N):
    while que and que[-1]<num[i]:
        que = que[:-1]
        cnt += 1
        if cnt == K:
            break
    if len(que)<N-K:
        que += num[i]
    if cnt == K:
        que += num[i+1:]
        break
print(que)
