import sys
N = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
N -= li.count(0)
ans = 0
max_2 = 0
for i in li:
    n = bin(i)[2:]
    ans += n.count('1')
    if max_2 < len(n):
        max_2 = len(n)
print(ans,max_2-1)


    
