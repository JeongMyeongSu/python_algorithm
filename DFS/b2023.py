N = int(input())
def primality(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
standard = 10**(N-1)
s1 = [2,3,5,7]
while not s1[0]//standard:
    t1 = s1.pop(0)
    for i in range(1,10,2):
        k=t1*10+i
        if primality(k):
            s1.append(k)
for i in s1:
    print(i)