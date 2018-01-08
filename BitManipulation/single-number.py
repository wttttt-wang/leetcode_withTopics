"""
Single Number
@ Bit Manipulation: The key point is a ^ a = 0
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for val in nums:
            res ^= val
        return res
