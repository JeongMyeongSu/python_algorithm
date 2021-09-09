T=int(input())
time=[300,60,10]
result=[]
for i in time:
    result.append(T//i)
    T=T%i
if T==0:
    for i in result:
        print(i, end=" ")
else:
    print(-1)