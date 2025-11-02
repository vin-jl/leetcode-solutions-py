class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        buy = [float('-inf')] * n # can start negative but we win these
        sell = [0] * n
        for i in range(0, n):
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]) # can sell anytime
            buy[i] = max(buy[i-1], sell[i-2] - prices[i]) # can only buy 2 days after selling

        return sell[n-1]
