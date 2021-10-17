from sys import stdin
N,M = map(int,stdin.readline().split())
now_park = [9999]+[0]*N
parklot = [0]
cost = 0
queue = []
for _ in range(N): # 단위무게당 요금
    Rs = int(stdin.readline())
    parklot.append(Rs)   # [0 2 3 5]
car = [0]
for _ in range(M): # 차 무게
    Wk = int(stdin.readline())
    car.append(Wk)        # [0 200 100 300 800]
for _ in range(2*M): # 출입
    io = int(stdin.readline())
    if io>0:
        for i in range(N+1):
            if now_park[i]==0:
                cost += car[io]*parklot[i]
                now_park[i]=io
                break
        else:
            queue.append(io)
    else:
        for i in range(N+1):
            if now_park[i]==-io:
                now_park[i] = 0
                if queue:
                    t = queue.pop(0)
                    now_park[i]=t
                    cost += car[t]*parklot[i]

print(cost)