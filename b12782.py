T = int(input())
for test_case in range(1,T+1):
    a,b = map(str,input().split())
    answer = len(a)
    counter=0
    counter_a=counter_b=0
    for i in range(len(a)):
        if a[i]==b[i]:
            answer -= 1
        else:
            if int(a[i]) > int(b[i]):
                counter_a += 1
            else:
                counter_b += 1
    if counter_a > counter_b:
        answer -= counter_b
    else:
        answer -= counter_a
         
    print(answer)