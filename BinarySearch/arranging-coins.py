"""
Arranging Coins
@ Binary Search
"""


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        left, right = 1, n
        while left < right - 1:
            mid = (right - left) / 2 + left
            val = mid * (mid + 1) / 2
            if val == n:
                return mid
            if val < n:
                left = mid
            else:
                right = mid
        return right if right * (right + 1) / 2 <= n else left
