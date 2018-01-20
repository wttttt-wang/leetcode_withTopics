"""
Happy Number
@ Hash
@ Also can solve like finding cycle in linkedList.
"""


class Solution(object):
    _dp = {1: True}

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n not in self._dp:
            occurs = set()
            while n > 1:
                n = self.calcu(n)
                if n in occurs:
                    self._dp[n] = False
                    return False
                occurs.add(n)
            self._dp[n] = True
        return self._dp[n]

    def calcu(self, n):
        res = 0
        while n:
            res += (n % 10) ** 2
            n /= 10
        return res

