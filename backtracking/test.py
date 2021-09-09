P=[1,2,3]
def p(n):
    if n == len(P):
        print(P)

    else:
        for i in range(n,3):
            P[i], P[n] = P[n], P[i]
            p(n+1)
            P[i], P[n] = P[n], P[i]
p(0)