T = int(input())
for test_case in range(1,T+1):
    sentence = input().split()
    print(f'Case #{test_case}:',end= " ")
    for i in range(len(sentence)):
        print(sentence.pop(-1),end =" ")