N,S = map(int,input().split())
num = list(map(int,input().split()))
cnt = 0
answer = []

def backtracking(n,part,bool):
    global answer
    if bool and sum(part)==S:
        answer.append(part)
    if n>=N:        
        return
    backtracking(n+1,part,False)
    backtracking(n+1,part+[num[n]],True)
backtracking(0,[],False)
print(len(answer))


