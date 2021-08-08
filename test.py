T=int(input())
li=list(map(int, input().split()))
li.sort()
print(f'{li[int((T-1)/2)]}')