from collections import deque # 재귀 시간초과
N = int(input())
stack1 = deque(list(map(int,input().split())))
stack2=deque()
stack3=deque()
k=0
change = []
def hanoi(n):
    global change
    if stack3 and stack3[-1]==n:
        return
    else:
        if stack1:
            while stack1: 
                if stack1[-1] == n:
                    stack3.append(stack1.pop())
                    change.append([1,3])
                    hanoi(n-1)
                    break
                else:
                    stack2.append(stack1.pop())
                    change.append([1,2])
        elif stack2:
            while 1: 
                if stack2[-1] == n:
                    stack3.append(stack2.pop())
                    change.append([2,3])
                    hanoi(n-1)
                    break
                else:
                    stack1.append(stack2.pop())
                    change.append([2,1])
hanoi(N)
print(len(change))
for i in change:
    print(*i)

