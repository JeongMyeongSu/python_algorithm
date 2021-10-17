import sys
N= int(input())
answer = ['0','1','2','3','4','5','6','7','8','9']
ans = 0
case = ['0','1','2','3','4','5','6','7','8','9']
def denum(number):
    global ans,answer
    print(number)
    if ans == N:
        print(number)
        sys.exit()
    elif ans >= N:
        return
    if len(number) == 0:
        for i in case:
            ans += 1
            denum(i)
    else:
        for i in case:
            new_number = number+i
            if new_number[-2]>new_number[-1]:
                answer.append(new_number)
                ans += 1
denum('')
print(answer[N])