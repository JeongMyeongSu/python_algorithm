import copy
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def coding(n,A,cnt):
    global min_cnt
    global min_cnt_arr
    if cnt>=min_cnt:
        return
    if n == 0:
        min_cnt = min(cnt,min_cnt)
        return
    r,c = code[n-1]
    for x in range(4):
        changed_arr = copy.deepcopy(A)
        changed_cnt = cnt
        flag = 0
        for l in range(1,N):
            dr = r+dx[x]*l
            dc = c+dy[x]*l
            if 0<=dr<N and 0<=dc<N:
                if changed_arr[dr][dc]==1:
                    flag=1
                    break
                else:
                    changed_cnt += 1
                    changed_arr[dr][dc]=1
        if not flag:
            if min_cnt_arr[n-1]>changed_cnt:
                min_cnt_arr[n-1] = changed_cnt
            coding(n-1,changed_arr,changed_cnt)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    code = []
    min_cnt = 987654321
    for i in range(N):
        hang = list(map(int,input().split()))
        arr.append(hang)
        for j in range(N):
            if hang[j]==1:
                code.append((i,j))
    min_cnt_arr = [100]*len(code)
    coding(len(code),arr,0)
    print(min_cnt_arr)
    for i in min_cnt_arr:
        if i != 100:
            print('#{} {}'.format(tc,i))
            break