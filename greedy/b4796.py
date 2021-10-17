from sys import stdin
t = 1
while 1:
    L,P,V = map(int,stdin.readline().split())
    if L+P+V == 0 :
        break
    answer = (V//P)*L
    answer += V%P if V%P < L else L
    print('Case {}: {}'.format(t,answer))
    t += 1