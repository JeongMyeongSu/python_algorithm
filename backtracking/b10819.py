N = int(input())
li = list(map(int,input().split()))
def logic(numbers):
    ans=0
    for i in range(len(numbers)-1):
        ans += abs(numbers[i]-numbers[i+1])
    return ans
answer=0
def swap(n):
    global answer
    if n == N:
        if logic(li)>answer:
            answer=logic(li)
        return
    else:
        for i in range(n,N):
            li[i],li[n] = li[n],li[i]
            swap(n+1)
            li[i],li[n] = li[n],li[i]
    return answer
print(swap(0))