N = int(input())
tops = list(map(int,input().split()))
stack = []
for i in range(len(tops)):
    j=1
    while i>=j and tops[i]>tops[i-j]:
        j += 1
    stack.append(i-j+1)
print(*stack)