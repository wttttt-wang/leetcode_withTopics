"""
Best Time to Buy and Sell Stock IV
@ dp: A typical usage of local & global optimal
@ 1. consider this problem as two situation: 1.1 must sell at day i; 1.2 not sell at day i.
                                                 so global optimal at day i is max(sell[i], not_sell[i])
  2. The key point is how to calculate sell[i][k] with O(1) time. First, u can consider sell at day i-1,
     and then buy at day i - 1, then sell at day i as one transaction.
     So sell[i][k] = max(sell[i - 1][k], global[i - 1][k - 1]) + prices[i] - prices[i - 1]
@ O(N * k) time, O(k) space
@ Corner case: if k > len(prices) / 2, then this can be considered as endless transaction allowed.
"""


class Solution(object):
    def maxProfit(self, m, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2 or m <= 0:
            return 0
        if m > len(prices) / 2:
            return self.maxProfit2(prices)
        # sell[i][k] = max(sell[i - 1][k], dp[i - 1][k - 1]) + prices[i] - prices[i - 1], stands for must sell at day i
        # dp[i][k] = max(sell[i][k], dp[i - 1][k]), dp[i][0] = 0, sell[i][0] = 0
        sell = [[0] * (m + 1) for _ in range(2)]
        dp = [[0] * (m + 1) for _ in range(2)]
        for i in range(1, len(prices)):
            for k in range(1, m + 1):
                sell[i % 2][k] = max(sell[(i - 1) % 2][k], dp[(i - 1) % 2][k - 1]) + prices[i] - prices[i - 1]
                dp[i % 2][k] = max(sell[i % 2][k], dp[(i - 1) % 2][k])
        return dp[(len(prices) - 1) % 2][m]

    def maxProfit2(self, prices):
        if not prices:
            return 0
        res = 0
        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i - 1])
        return res
