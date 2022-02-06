import sys
N = int(sys.stdin.readline())
buildings = [int(sys.stdin.readline()) for _ in range(N)]
ans = 0
stack = []
for i in range(len(buildings)):
    while stack and stack[-1]<=buildings[i]:
        stack.pop()
    stack.append(buildings[i])
    ans += len(stack)-1
print(ans)
    
            