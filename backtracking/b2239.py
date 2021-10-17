import sys
arr = [list(map(int,input())) for _ in range(9)]

def check(r,c,x):
    if x in arr[r]:
        return False
    for i in range(9):
        if arr[i][c] == x:
            return False

    dr = r//3
    dc = c//3
    for i in range(3*dr,3*dr+3):
        for j in range(3*dc,3*dc+3):
            if x == arr[i][j]:
                return False
    return True

def sdoku():
    flag = 0
    for i in range(9):
        for j in range(9):
            if arr[i][j]==0:
                r,c = i,j
                flag = 1
                break
        if flag:
            break

    if not flag:
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end='')
            print()
        exit()
        return
    
    for x in range(1,10):
        if check(r,c,x):
            arr[r][c]=x
            sdoku()
            arr[r][c]=0

sdoku()
