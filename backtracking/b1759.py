L,C = map(int,input().split())
letters = list(map(str,input().split()))
letters.sort()
answer=[]
moeum={'a','e','i','o','u'}
def password(s,i):
    global answer
    if len(s)==L and (moeum&set(s)) and len([x for x in s if x not in moeum])>1:
        answer.append(s)
    elif i==C:
        return
    else:
        if i < C:
            password(s+letters[i],i+1)
        if i < C:
            password(s,i+1)
password('',0)
for i in answer:
    print(i)