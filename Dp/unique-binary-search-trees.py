"""
Unique Binary Search Trees
@ dp
"""


class Solution(object):
    _dp = {1: 1, 0: 1}

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        return self.helper(n)

    def helper(self, n):
        dp = self._dp
        if n not in dp:
            res = 0
            for i in range(n):
                res += self.helper(i) * self.helper(n - i - 1)
            dp[n] = res
        return dp[n]
