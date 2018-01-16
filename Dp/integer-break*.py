"""
Integer Break
@ dp: The way of dp is easy. But pay attention that "at least two positive integers". This is why we need 'helper()'
"""


class Solution(object):
    dp = {1: 1}

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        for i in range(1, n):
            res = max(res, i * self.helper(n - i))
        return res

    def helper(self, n):
        if n not in self.dp:
            res = n
            for x in range(1, n):
                res = max(res, x * self.helper(n - x))
            self.dp[n] = res
        return self.dp[n]
