def maxProfit(prices):
    # to maximize profit, we buy at a local min and sell at a local max to capture profit

    # Time: O(n), n is length of prices
    # Space: O(1)
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += (
                prices[i] - prices[i - 1]
            )  # whenever there is an increase, add to the profit
    return profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # 7

prices = [1, 2, 3, 4, 5]
print(maxProfit(prices))  # 4

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))  # 0
