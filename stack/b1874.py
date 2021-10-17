from collections import deque
N =int(input())
numbers = [int(input()) for _ in range(N)]
stack = deque()
j = 0
cnt = 0
flag = 0
answer = []
for i in range(1,N+1):
    stack.append(i)
    answer.append('+')
    cnt += 1
    while stack and numbers[j] == stack[-1]:
        stack.pop()
        j += 1
        answer.append('-')
        cnt += 1
if len(answer) == 2*N:
    for i in range(len(answer)):
        print(answer[i])
else:
    print('NO')