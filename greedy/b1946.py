import sys
T = int(input())
for tc in range(T):
    N = int(input())
    grades=[]
    for _ in range(N):
        grade= list(map(int,sys.stdin.readline().split()))
        grades.append(grade)
    grades.sort()
    cnt = 1
    ming = grades[0][1]
    for i in range(1,N):
        if grades[i][1] < ming:
            ming = grades[i][1]
            cnt += 1
    print(cnt)