"""
Single Number III
@ Bit Manipulation: 1. a xor a = 0. assume results = [A, B], we xor all elements in nums and get x, then x = A xor B
                    2. split A, B into two parts: using low_bit of x as split flag. (use x & (-x) to get low bit of x)
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        for val in nums:
            x ^= val
        # to get low bit, can also: low_bit = x & (-x)
        low_bit = x - (x & (x - 1))  # assume results = [A, B], then x = A xor B
        # split to two group, according to low_bit, this will split two results into two diff parts
        res = [0, 0]
        for val in nums:
            if val & low_bit:
                res[0] ^= val
            else:
                res[1] ^= val
        return res
