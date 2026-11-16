class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use two pointers to keep the diffrerence
        max_profit = 0
        i = 0
        j = len(prices) -1
        while i < j:
            profit = prices[i] * -1 + prices[j]
            max_profit = max(max_profit, profit)
            i += 1
            j -= 1

        return max_profit
