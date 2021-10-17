def p(n,nums):
    if n > k:
        return
    if 6 == len(nums):
        print(*nums)
        return
    else:
        if n < k:
            p(n+1,nums+[li[n]])
        if n < k:
            p(n+1,nums)  
while 1:
    li = list(map(int,input().split()))
    k = li.pop(0)
    if k==0:
        break
    p(0,[])
    print()
