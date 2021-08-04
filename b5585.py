a=int(input())
rest=1000-a
count=0
money=[500,100,50,10,5,1]
while rest!=0:
    if rest>=money[0]:
        rest-=money[0]
        count+=1
    else:
        money.remove(money[0])
print(count)