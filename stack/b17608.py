import sys
N = int(input())
height = [int(sys.stdin.readline())]
for i in range(N-1):
    height.append(int(sys.stdin.readline()))
answer = 1
max_height = height[-1]
for i in height[::-1]:
    if i>max_height:
        answer += 1
        max_height = i
print(answer)