def ftree(n):
    if n:
        print(chr(n+64),end='')
        ftree(left[n])
        ftree(right[n])
def mtree(n):
    if n:
        mtree(left[n])
        print(chr(n+64),end='')
        mtree(right[n])
def btree(n):
    if n:
        btree(left[n])
        btree(right[n])
        print(chr(n+64),end='')

N = int(input())
left = [0]*(N+1)
right = [0]*(N+1)

for _ in range(N):
    p,l,r = map(lambda x:ord(x)-ord('A')+1, input().split())
    if l>0:
        left[p] = l
    if r>0:
        right[p] = r
ftree(1)
print()
mtree(1)
print()
btree(1)