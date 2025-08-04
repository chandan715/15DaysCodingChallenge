def maxProfit(prices):
    min_price = float('inf')
    profit = 0
    for i in prices:
     if i < min_price:
        min_price = i
     else:
        profit = max(profit, i - min_price)
    return profit
x=[7,1,3,5,6,4]
print(maxProfit(x))