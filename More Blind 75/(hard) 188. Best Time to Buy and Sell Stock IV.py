class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        if not prices or k == 0:
            return 0
        
        n = len(prices)
        if k >= n // 2:
            # 如果k的值大于等于n的一半，相当于可以进行任意次交易，直接使用贪心算法解决
            max_profit = 0
            for i in range(1, n):
                max_profit += max(0, prices[i] - prices[i - 1])
            return max_profit
        
        dp = [[0] * (k + 1) for _ in range(n)]
        
        for j in range(1, k + 1):
            max_diff = -prices[0]
            for i in range(1, n):
                dp[i][j] = max(dp[i - 1][j], prices[i] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j - 1] - prices[i])

        print(dp)
        
        return dp[-1][-1]
