from sys import stdin

N = int(stdin.readline())
li=[]
def action(word):
    if word[0] == 'push':
        li.append(int(word[1]))
    if word[0] == 'pop':
        if li:
            print(li.pop(0))
        else:
            print(-1)
    if word[0]=='size':
        print(len(li))
    if word[0]=='empty':
        if li:
            print(0)
        else:
            print(1)
    if word[0]=='front':
        print(li[0])
    if word[0]=='back':
        print(li[-1])

for _ in range(N):
    x = stdin.readline().split()
    action(x)
    