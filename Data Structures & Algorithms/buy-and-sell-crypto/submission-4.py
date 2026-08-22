class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= bestBuy:
                profit = max(profit, prices[i] - bestBuy)
                continue
            bestBuy = prices[i]
        return profit
    