from collections import deque
T= int(input())
for tc in range(1,T+1):
    N,target = map(int,input().split())
    importance = deque(list(map(int,input().split())))
    cnt = 0
    while importance:
        if importance[0] == max(importance):
            importance.popleft()
            cnt += 1
            if target == 0:
                break
        else:
            importance.rotate(-1)
        target -= 1
        if target<0:
            target = len(importance)-1
    print(cnt)