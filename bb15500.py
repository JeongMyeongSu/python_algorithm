n = int(input())
stack1 = list(map(int,input().split()))
stack2=[]
stack3=[]
change = []
while n>0:
    while n in stack1: 
        if stack1[-1] == n:
            stack3.append(stack1.pop())
            change.append([1,3])
            n -= 1
        else:
            stack2.append(stack1.pop())
            change.append([1,2])
    
    while n in stack2: 
        if stack2[-1] == n:
            stack3.append(stack2.pop())
            change.append([2,3])
            n -= 1
        else:
            stack1.append(stack2.pop())
            change.append([2,1])
print(len(change))
for i in change:
    print(*i)