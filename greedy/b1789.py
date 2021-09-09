S=int(input())
i=1
while 1:
    if S < i*(i+1)/2:
        print(i-1)
        break
    else:
        i+=1