"""
Guess Number Higher or Lower
@ Binary Search
"""


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return
        left, right = 1, n
        while left < right - 1:
            mid = (right - left) / 2 + left
            flag = guess(mid)
            if not flag:
                return mid
            if flag == 1:
                left = mid
            else:
                right = mid
        return left if not guess(left) else right
