import sys
N = int(sys.stdin.readline())
max_height = 0
max_idx= 0
buildings = []
max_i = 0
for _ in range(N):
    i, height = map(int,sys.stdin.readline().split())
    buildings.append((i,height))
    if height>max_height:
        max_height = height
        max_idx = i
buildings.sort()
now = buildings[0]
ans = 0
for building in buildings:
    if building[1] >= now[1]:
        ans += (building[0]-now[0])*now[1]
        now = building
        if now[0] == max_idx:
            break
now = buildings[-1]
for building in buildings[::-1]:
    if building[1] >= now[1]:
        ans += (now[0]-building[0])*now[1]
        now = building
        if now[0] == max_idx:
            break
ans += max_height 
print(ans)



    




