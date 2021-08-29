T = int(input())
stack=[]
for _ in range(T):
    N = int(input())
    if N == 0:
        stack.pop()
    else:
        stack.append(N)
answer = 0
for i in stack:
    answer += i
print(answer)
