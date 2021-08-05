N=int(input())
x=N//5
count=N//3+1
counter=0
for i in range(x+1):
    if (N-5*i)%3==0:
        if i+(N-5*i)/3 < count:
            count=int(i+(N-5*i)/3)
            counter+=1
if counter==0:
    print(-1)
else:
    print(count)

