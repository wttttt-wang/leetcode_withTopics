"""
Valid Perfect Square
@ Binary Search
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num or num < 1:
            return False
        left, right = 1, num
        while left < right - 1:
            mid = (right - left) / 2 + left
            val = mid ** 2
            if val == num:
                return True
            if val < num:
                left = mid
            else:
                right = mid
        return left ** 2 == num or right ** 2 == num
