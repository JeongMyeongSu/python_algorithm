s, number  = map(int,input().split())
counter = 1
while number > s:
    if number%2==0:
        number /= 2
        counter += 1
    elif number%10 == 1:
        number //= 10
        counter += 1
    else:
        break
if s==number:
    print(counter)
else:
    print(-1)

    