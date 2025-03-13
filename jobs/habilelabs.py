def max_profit(prices):
    min_price = float('inf')  # Track lowest price seen so far
    max_profit = 0            # Track max profit

    for price in prices:
        min_price = min(min_price, price)  # Update minimum price
        max_profit = max(max_profit, price - min_price)  # Update profit

    return max_profit if max_profit > 0 else "No Profit"

prices = [2, 5]
result = max_profit(prices)
print(result)  # Output: 3
