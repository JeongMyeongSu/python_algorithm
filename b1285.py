T=int(input())
coins=[]
counter=0
for i in range(T):
    li=input()
    coins.append(list(li))
    counter+=li.count("T")
coins_copy=coins
for coin in coins:
    if coin.count("T")>=coin.count("H"):
        for i in range(len(coin)):
            if coin[i]=="T":
                coin[i]="H"
            else:
                coin[i]="T"

coins=list(zip(*coins))
for coin in coins:
    if coin.count("T")>=coin.count("H"):
        for i in range(len(coin)):
            if coin[i]=="T":
                coin[i]="H"
            else:
                coin[i]="T"

coins_copy=list(zip(*coins_copy))
for coin in coins_copy:
    if coin.count("T")>=coin.count("H"):
        for i in range(len(coin)):
            if coin[i]=="T":
                coin[i]="H"
            else:
                coin[i]="T"
coins_copy=list(zip(*coins_copy))
for coin in coins_copy:
    if coin.count("T")>=coin.count("H"):
        for i in range(len(coin)):
            if coin[i]=="T":
                coin[i]="H"
            else:
                coin[i]="T"


print(coins_copy)

    