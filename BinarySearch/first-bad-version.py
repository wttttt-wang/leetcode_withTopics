"""
First Bad Version
@ Binary Search
"""


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return
        # left-most bad
        left, right = 1, n
        while left < right - 1:
            mid = (right - left) / 2 + left
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        return left if isBadVersion(left) else right
