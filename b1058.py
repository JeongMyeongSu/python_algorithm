N = int(input())
arr = [list(input()) for _ in range(N)]
max_friends = 0
for i in range(N):
    friends = 0
    f_list = [0]*(N+1)
    for j in range(N):
        if arr[i][j] == 'Y' and f_list[j] == 0:
            friends += 1
            f_list[j] = 1
            for k in range(N):
                if arr[k][j] == 'Y' and f_list[k] == 0 and i != k:
                    friends += 1
                    f_list[k] = 1
    if friends>max_friends:
        max_friends = friends
print(max_friends)


        

