import sys
N = int(sys.stdin.readline())
buildings = [int(sys.stdin.readline()) for _ in range(N)]
ans = 0
stack = []
for i in buildings[::-1]:
    if stack:
        if stack[0]<i:
            stack.append(i)
        else:
            ans += len(stack)
            stack = []
    else:
        stack.append(i)
print(ans)