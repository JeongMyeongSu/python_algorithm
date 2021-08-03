N=int(input())
each_time=sorted(list(map(int,input().split())))
sum=0
for i in range(len(each_time)):
    sum+=(len(each_time)-i)*each_time[i]
print(sum)