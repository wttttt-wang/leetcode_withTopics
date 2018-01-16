"""
Coin Change
@ dp: Nothing special.
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not amount:
            return 0
        if not coins:
            return -1
        dp = [0]
        for i in range(1, amount + 1):
            tmp = sys.maxint
            for v in coins:
                if i - v >= 0 and dp[i - v] != -1:
                    tmp = min(tmp, dp[i - v] + 1)
            if tmp == sys.maxint:
                dp.append(-1)
            else:
                dp.append(tmp)
        return dp[amount]
