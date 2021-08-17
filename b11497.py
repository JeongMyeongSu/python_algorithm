T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    li = list(map(int,input().split()))
    li.sort()
    print(li)
    li2 = []
    for i in range(len(li)-2):
        li2.append((li[i+1]-li[i])+(li[i+2]-li[i+1]))
    print(max(li2))
