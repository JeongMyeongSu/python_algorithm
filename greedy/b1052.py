import sys
N, K = map(int,sys.stdin.readline().split())
ans = 0
while bin(N)[2:].count('1')>K:
    a = 2**(bin(N)[::-1].index('1'))
    ans += a
    N += a
print(ans)
    