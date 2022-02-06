import sys
sys.stdin = open('input1.txt')

def time_checker(li):
    visit = [0]*200
    max_time = 0
    for k in li:
        while 1:
            if not visit[k]:
                visit[k]=1
                if max_time<k:
                    max_time=k
                break
            else:
                k += 1
    return max_time

def choice(i,li1,li2):
    global min_time
    # if i > len(person)-1 :
    if len(li1)+len(li2)==len(person):
        time = max(time_checker(li1),time_checker(li2))
        min_time = min(time,min_time)
        return
    choice(i+1,li1,li2+[case2[i]])
    choice(i+1,li1+[case1[i]],li2)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    person=[]
    exs=[]
    min_time = 987654321
    for i in range(N):
        hang = list(map(int,input().split()))
        for j in range(N):
            if hang[j]==1:
                person.append((i,j))
            elif hang[j]==2:
                exs.append((i,j))
    case1 = []
    case2=[]
    ex_i1,ex_j1 = exs[0]
    ex_i2,ex_j2 = exs[1]
    for i,j in person:
        distance1 = abs(ex_i1-i)+abs(ex_j1-j)
        case1.append(distance1)
        distance2 = abs(ex_i2-i)+abs(ex_j2-j)
        case2.append(distance2)
    test1 = []
    test2 = []
    choice(0,test1,test2)
    print(f'#{tc} {min_time+1}')