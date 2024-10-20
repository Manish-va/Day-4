def maxProfit(prices):
    # Initialize total maximum profit to 0
    max_profit = 0
    # Start from the second price
    for i in range(1, len(prices)):
        # Check if the current price is greater than the previous price
        if prices[i] > prices[i - 1]:
            # Add the profit from this transaction
            max_profit += prices[i] - prices[i - 1]
    # Return the total maximum profit
    return max_profit
print(maxProfit([1,2,3,4,5])) 
print(maxProfit([7,1,5,3,6,4]))
