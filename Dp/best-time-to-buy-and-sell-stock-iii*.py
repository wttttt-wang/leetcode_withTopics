"""
Best Time to Buy and Sell Stock III
@ dp  + Forward & backward traverse
@ O(N) time  & space
@ Note: For solution with O(1) space please see Solution2 below.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        backMax = [0] * len(prices)
        tmpMax = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            backMax[i] = max(backMax[i + 1], tmpMax - prices[i])
            tmpMax = max(tmpMax, prices[i])
        res = backMax[0]
        tmpMin = prices[0]
        forMaxBefore = 0
        for i in range(1, len(prices)):
            forMaxBefore = max(forMaxBefore, prices[i] - tmpMin)
            res = max(res, forMaxBefore + backMax[i])
            tmpMin = min(tmpMin, prices[i])
        return res


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy1, buy2 = -sys.maxint, -sys.maxint
        sell1, sell2 = 0, 0
        for val in prices:
            sell2 = max(sell2, buy2 + val)
            buy2 = max(buy2, sell1 - val)
            sell1 = max(sell1, buy1 + val)
            buy1 = max(buy1, -val)
        return sell2

