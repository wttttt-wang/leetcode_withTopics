"""
Number of 1 Bits
@ Bit Manipulation: Very basic.
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        res = 0
        for i in range(32):
            res += (n & 1)
            n >>= 1
        return res
