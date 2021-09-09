a = list(input())
stack=[]
for i in range(len(a)):
    if a[i] == '(' or '[':
        stack.append(a[i])
    elif a[i] == ')':
        if stack and stack[-1]=='(':
            stack.pop()
            stack.append(2)
    elif a[i] == ']':
        if stack and stack[-1]=='[':
            stack.pop()
            stack.append(3)
print(stack)
