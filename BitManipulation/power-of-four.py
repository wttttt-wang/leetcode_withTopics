"""
Power of Four
@ Bit Manipulation
"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 or (num & (num - 1)) != 0:
            return False
        # check if low bit is in even position
        num &= (-num)
        for i in range(32):
            if num & 1:
                return False if i % 2 else True
            num >>= 1
        return False
