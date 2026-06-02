def maxProfit(prices):

    max_profit = 0

    for i in range(1, len(prices)):
        for j in range(i+1, len(prices)):

            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
            
    return max_profit
    
print(maxProfit([7,1,5,3,6,4]))  # should be 5
print(maxProfit([7,6,4,3,1]))    # should be 0 (prices only go down)
