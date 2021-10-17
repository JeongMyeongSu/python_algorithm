N, K = map(int,input().split())
order = list(map(int,input().split()))
def sorting(x,i):
    if x in order[i+1:]:
        return order[i+1:].index(x)
    else:
        return 100
cnt = 0
tap = []
for i in range(K):
    if order[i] not in tap:
        tap.sort(key=lambda x:sorting(x,i))
        tap.insert(0,order[i])
        if len(tap)>N:
            tap.pop()
            cnt += 1
    else:
        continue
print(cnt)
