#best time to buy and sell
def buysell( prices):
    left=0
    max_profit=0
    for right in range(len(arr)):
        if prices[left]<prices[right]:
            profit=prices[right]-prices[left]
            max_profit=max(max_profit, profit)
        else:
            left=right
    return max_profit
prices=[7, 1,5 ,3 ,6,4]
print(buysell(prices))
