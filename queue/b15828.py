from sys import stdin
N = int(stdin.readline())
queue = []
while 1:
    k = int(stdin.readline())
    if k == -1:
        break
    elif k == 0:
        queue.pop(0)
    else:
        if len(queue)==N:
            continue
        else:
            queue.append(k)
if queue:
    print(*queue)
else:
    print('empty')