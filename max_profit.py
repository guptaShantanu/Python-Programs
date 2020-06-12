def findMax(start,price):
    maxi=price[start]
    loc=start
    for i in range(start,len(price)):
        if price[i]>=maxi:
            maxi=price[i]
            loc = i
    return loc


def maximumProfit(price):
    target = 0
    profit=0
    i=0
    while True:
        temp = findMax(i,price)
        print(price[temp])
        if temp==i:
            i+=1
            continue
        else:
            for j in range(target,temp):
                if price[j]<=price[temp]:
                    profit+=price[temp]-price[j]
            target = temp+1
            i=temp+1
        if i>=len(price):
            break

    return profit

print(maximumProfit([5,3,2]))
