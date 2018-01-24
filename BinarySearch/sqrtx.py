"""
Sqrt(x)
@ Binary Search
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return 0
        left, right = 1, x  # find right-most <=
        while left < right - 1:
            mid = (right - left) / 2 + left
            val = mid ** 2
            if val == x:
                return mid
            if val < x:
                left = mid
            else:
                right = mid
        if right ** 2 <= x:
            return right
        return left
