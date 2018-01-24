"""
Pow(x, n)
@ Math + (dp): The basic idea is simple. But should pay attention to the corner cases!!!
@ Corner case: 1. n <= 0 (We cannot just use abs(n) and then 1/x, for it will overflow(overflow even for type long))
                  e.g: x = 2.0000, n = -2147483648
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return self.helper(x, n, {1: x, 0: 1, -1: 1 / x})

    def helper(self, x, n, dp):
        if n not in dp:
            val = self.helper(x, (n - 1) / 2, dp) * self.helper(x, (n + 1) / 2, dp) if n % 2 else (self.helper(x, n / 2,
                                                                                                               dp)) ** 2
            dp[n] = val
        return dp[n]
