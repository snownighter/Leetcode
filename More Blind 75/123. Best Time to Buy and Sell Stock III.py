class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        n = len(prices)
        hold1 = [-prices[0]] + [0] * (n - 1)
        sold1 = [0] * n
        hold2 = [-prices[0]] + [0] * (n - 1)
        sold2 = [0] * n

        for i in range(1, n):
            hold1[i] = max(hold1[i - 1], -prices[i])
            sold1[i] = max(sold1[i - 1], hold1[i - 1] + prices[i])
            hold2[i] = max(hold2[i - 1], sold1[i - 1] - prices[i])
            sold2[i] = max(sold2[i - 1], hold2[i - 1] + prices[i])

        return sold2[-1]
