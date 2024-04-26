class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n <= 1:
            return 0
        
        hold, sold, cooldown = -prices[0], 0, 0
        
        for i in range(1, n):
            hold, sold, cooldown = max(hold, cooldown - prices[i]), hold + prices[i], max(sold, cooldown)
        
        return max(sold, cooldown)
