"""
Integer Replacement
@ dp / Memorization
"""


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        dp = {1: 0}
        return self.helper(n, dp)

    def helper(self, n, dp):
        if n not in dp:
            if n % 2:
                dp[n] = min(self.helper(n - 1, dp), self.helper(n + 1, dp)) + 1
            else:
                dp[n] = self.helper(n / 2, dp) + 1
        return dp[n]

