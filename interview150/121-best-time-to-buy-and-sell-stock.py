def maxProfit(prices):
    # Time: O(n), n is length of prices
    # Space: O(1)
    minPrice = float("inf")
    maxProfit = 0
    for price in prices:
        minPrice = min(minPrice, price)
        profit = price - minPrice
        maxProfit = max(maxProfit, profit)
    return maxProfit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # 5

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))  # 0
