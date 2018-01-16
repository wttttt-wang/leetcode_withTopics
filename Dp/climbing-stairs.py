"""
Climbing Stairs
@ dp
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        # dp, dp[i] = dp[i - 1] + dp[i - 2]
        dp = [1, 1, 1]
        for i in range(2, n + 1):
            dp[i % 3] = dp[(i - 1) % 3] + dp[(i - 2) % 3]
        return dp[n % 3]
