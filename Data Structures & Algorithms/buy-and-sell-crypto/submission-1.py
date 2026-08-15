class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_buy = prices[0]
        for i in range(1,len(prices)):
            if prices[i] - best_buy > max_profit:
                max_profit = prices[i] - best_buy
            if prices[i] < best_buy:
                best_buy = prices[i]
        return max_profit 