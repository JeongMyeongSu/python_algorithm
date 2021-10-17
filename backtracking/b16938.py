import sys
N,L,R,X = map(int,sys.stdin.readline().split())
A = sorted(list(map(int,sys.stdin.readline().split())))
cnt = 0
def backtracking(n,score):
    global cnt
    if sum(score) > R:
        return
    if n == N:
        if L<=sum(score) and max(score)-min(score)>=X:
            cnt += 1
        return
    backtracking(n+1,score+[A[n]])
    backtracking(n+1,score)
backtracking(0,[])
print(cnt)

    