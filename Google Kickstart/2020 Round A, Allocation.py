for i in range(int(input())):
    num_houses,budget=input().split()
    budget = int(budget)
    house_prices = input().split()
    house_prices.sort()
    houses_bought = 0
    while budget >= int(house_prices[0]):
        budget -= int(house_prices[0])
        house_prices.pop(0)
        houses_bought+=1
    print("Case #"+str(i+1)+": "+str(houses_bought))
        
