import sys
N = int(input())
cnt = -1
def back(n):
    global cnt
    cnt += 1
    print(n)
    if cnt == N:
        sys.exit()
    cnt += 1
    cnt -= 1
    if not n:
        for i in range(10):
            if not n:
                n = str(i)
                back(n)
                n = ''
    else:
        for i in range(10):
            if n[-1] <= str(i):
                continue
            n += str(i)
            print(n)
            back(n)
            n = n[:-1]

back('')