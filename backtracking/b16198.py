N = int(input())
num = list(map(int,input().split()))
max_energy=0
def backtracking(li,energy):
    global max_energy
    if len(li)==2:
        if energy>max_energy:
            max_energy=energy
        return
    else:
        for i in range(1,len(li)-1):
            plus = li[i-1]*li[i+1]
            a = li.pop(i)
            backtracking(li,energy+plus)
            li.insert(i,a)
backtracking(num,0)
print(max_energy)


