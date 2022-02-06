import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(2**N)]
L = list(map(int,input().split()))
size = 2**N
def down(A):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    check=[]
    for i in range(size):
        for j in range(size):
            cnt = 0
            for x in range(4):
                di = i+dx[x]
                dj = j+dy[x]
                if 0<=di<size and 0<=dj<size and A[di][dj] > 0:
                    cnt += 1
            if cnt<3:
                check.append((i,j))
    for i,j in check:
        if A[i][j]>0:
            A[i][j] -= 1
def big(A):
    bigsize = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    check = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if A[i][j] and not check[i][j]:
                q=[(i,j)]
                counter = 1
                check[i][j]=1
                while q:
                    a,b = q.pop(0)
                    for x in range(4):
                        di = a+dx[x]
                        dj = b+dy[x]
                        if 0<=di<size and 0<=dj<size and A[di][dj] and not check[di][dj]:
                            check[di][dj] = 1
                            counter += 1
                            q.append((di,dj))
                            if bigsize<counter:
                                bigsize=counter
    return bigsize

for q in range(len(L)):
    meteo = 2**L[q]
    new_arr = [[0]*size for _ in range(size)]
    for r in range(0,size,meteo):
        for c in range(0,size,meteo):
            for i in range(meteo):
                for j in range(meteo):
                    new_arr[r+i][c+j] = arr[r+meteo-1-j][c+i]
    down(new_arr)
    arr = new_arr
answer = 0
for x in arr:
    answer += sum(x)

print(answer)
print(big(arr))
