T = int(input())
for tc in range(1,T+1):
    N = int(input())
    P = list(map(int,input().split()))
    stack = []
    answer = []
    for i in P:
        if stack and (i in stack):
            stack.pop(0)
        else:
            answer.append(i)
            stack.append((i*4)//3)
    print('Case #{}:'.format(tc), end = ' ')
    print(*answer)

        
