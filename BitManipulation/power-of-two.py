"""
Power of Two
@ Bit Manipulation: 1. power of two --> only one 1 digit in binary presentation of n.
                    2. use n & (n - 1) to put the right-most 1 bit to 0 bit.
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n - 1) == 0

