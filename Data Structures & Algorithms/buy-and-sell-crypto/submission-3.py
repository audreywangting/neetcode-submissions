class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterate the list
        # keep a minimum buying price
        # keep comparing and updating the profit
        # max(profit = profit[today] - minimum buying price)

        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit
        
        