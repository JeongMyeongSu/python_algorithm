import sys
sys.stdin = open('input.txt')

def couple(A,i):
    global max_eff
    if len(A)==4:
        a,b,c,d = A
        if abs(d-a)>N-2:
            return
        cnt = 0
        if a<c and c<b:
            cnt += 1
        if a<d and d<b:
            cnt += 1
        if cnt == 1:
            return
        hap = (circle[a]+circle[b])**2+(circle[c]+circle[d])**2
        if hap>max_eff:
            max_eff = hap
        return
    for j in range(i+2,N):
        couple(A+[j],j)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    circle = list(map(int,input().split()))
    max_eff = 0
    for _ in range(N):
        x = circle[0]
        del circle[0]
        circle.append(x)
        couple([0],0)
    print('#{} {}'.format(tc,max_eff))