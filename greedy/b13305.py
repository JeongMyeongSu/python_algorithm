N = int(input())
distances = list(map(int, input().split()))
price = list(map(int, input().split()))
money = 0
min_price = price[0]
for i in range(len(distances)):
    if i == 0:
        money += distances[i]*min_price
    else:
        if price[i] > min_price:
            money += min_price*distances[i]
        else:
            min_price = price[i]
            money += min_price*distances[i]
print(money)

