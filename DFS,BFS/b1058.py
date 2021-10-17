N = int(input())
arr = [list(input()) for _ in range(N)]
max_friends = 0
for i in range(N):
    friends = 0
    f_list = [0]*N
    for j in range(N):
        if arr[i][j] == 'Y':
            f_list[j] = 1
            for k in range(N):
                if arr[k][j] == 'Y':
                    f_list[k] = 1
    f_list[i]=0
    friends = sum(f_list)
    if friends>max_friends:
        max_friends = friends
print(max_friends)

