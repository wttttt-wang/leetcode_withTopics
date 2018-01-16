"""
Best Time to Buy and Sell Stock with Cooldown
@ dp: 1. states: sell, buy, rest(cool down)
      2. transition:
                 buy[i] = max(buy[i - 1], rest[i - 1] - prices[i - 1])
                 sell[i] = max(sell[i - 1], buy[i - 1] + prices[i - 1])
                 rest[i] = max(rest[i - 1], buy[i - 1], sell[i - 1])
         And rest[i] = sell[i - 1], so:
         buy[i] = max(buy[i - 1], sell[i - 2] - prices[i - 1])
         sell[i] = max(sell[i - 1], buy[i - 1] + prices[i - 1])
@ refer: https://discuss.leetcode.com/topic/30421/share-my-thinking-process
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        buy, sell = [-prices[0], 0, 0], [0, 0, 0]
        for i in range(1, len(prices)):
            sell[i % 3] = max(sell[(i - 1) % 3], buy[(i - 1) % 3] + prices[i])
            buy[i % 3] = max(buy[(i - 1) % 3], sell[(i - 2) % 3] - prices[i])
        return sell[(len(prices) - 1) % 3]
