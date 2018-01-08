"""
Best Time to Buy and Sell Stock
@ Easy dp
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        res, minVal = 0, prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - minVal)
            minVal = min(minVal, prices[i])
        return res
