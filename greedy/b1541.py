T=input()
li=[]
while '+' in T or '-' in T:
    try:
        if T.index('+')<T.index('-'):
            if '+' in T:
              li.append(int(T[:T.index('+')]))
              li.append('+')
              T=T[T.index('+')+1:]
              continue
        if '-' in T:
            li.append(int(T[:T.index('-')]))
            li.append('-')
            T=T[T.index('-')+1:]

    except:
            
        if '+' in T:
            li.append(int(T[:T.index('+')]))
            li.append('+')
            T=T[T.index('+')+1:]
            continue
        if '-' in T:
            li.append(int(T[:T.index('-')]))
            li.append('-')
            T=T[T.index('-')+1:]
li.append(int(T))
sum_li=0
plus_mode=1
for i in li:
    if i=='-':
        plus_mode=0
    if type(i)== int:
        if plus_mode==1:
            sum_li+=i
        else:
            sum_li-=i
print(sum_li)