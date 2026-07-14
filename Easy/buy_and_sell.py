
prices = [2, 6, 6, 1, 4, 1, 7]

min_price = prices[0]
profit = 0

for i in range(1, len(prices)):
    curr_profit = prices[i] - min_price
    if curr_profit > profit:
        profit = curr_profit
    min_price = min(min_price, prices[i])
print(profit)
