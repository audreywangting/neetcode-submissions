class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy:
        """
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            profit = price - min_price
            max_profit = max(profit, max_profit)
            min_price = min(price, min_price)

        return max_profit
        """
        # sliding window
        # left: current min price to buy
        # right: current position
        left = 0
        max_profit = 0
        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

        return max_profit


