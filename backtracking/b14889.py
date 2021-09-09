N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
cases=[]
def team(i,n):
    global cases
    if len(n)==N//2:
        cases.append(n)
    else:
        if i < N-1:
            team(i+1,n+[i+1])
        if i < N-2:
            team(i+1,n)
team(0,[0])
answer=999
all_case = list(range(N))
for case in cases:
    case2 = [x for x in all_case if x not in case]
    case_x=0
    case_y=0
    for i in case:
        for j in case:
            case_x += arr[i][j]
    for i in case2:
        for j in case2:
            case_y += arr[i][j]
    gap = abs(case_x-case_y)
    
    if gap<answer:
        answer = gap
print(answer)