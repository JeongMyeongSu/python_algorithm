import sys
N,K = map(int,sys.stdin.readline().split())
books = list(map(int,sys.stdin.readline().split()))
underbooks = []
upperbooks = []
for i in books:
    if i>0:
        upperbooks.append(i)
    else:
        underbooks.append(-i)
underbooks.sort()
upperbooks.sort()

ans = 0
if underbooks and upperbooks:
    last = max(underbooks[-1],upperbooks[-1])
elif underbooks:
    last = underbooks[-1]
elif upperbooks:
    last = upperbooks[-1]

while upperbooks:
    ans += upperbooks[-1]*2
    for _ in range(K):
        if upperbooks:
            del upperbooks[-1]
while underbooks:
    ans += underbooks[-1]*2
    for _ in range(K):
        if underbooks:
            del underbooks[-1]
ans -= last
print(ans)