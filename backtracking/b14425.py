N,M = map(int,input().split())
words = set()
for _ in range(N):
    words.add(input())
cnt = 0
for _ in range(M):
    x = input()
    if x in words:
        cnt += 1
print(cnt)