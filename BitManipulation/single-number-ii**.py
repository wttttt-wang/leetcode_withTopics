"""
Single Number II
@ Bit Manipulation: 1. calculate the number of 1 in each bit.
                    2. For each bit, the number of 1 should % 3
"""


class SolutionV2(object):
    def singleNumber(self, nums):
        ones, twos = 0, 0  # for each bit in ones(twos), 1 stands for current index has one(two) 1 bit.
        for val in nums:
            # first appear --> save it in ones;  third time --> try to save in ones but value saved in twos clear it.
            ones = (ones ^ val) & ~twos
            twos = (twos ^ val) & ~ones  # clear ones but save in twos for later check
        return ones


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            tmpSum = 0
            for val in nums:
                tmpSum += (val >> i) & 1
            res += (tmpSum % 3) << i
        return self.convert(res)

    def convert(self, x):
        if x >= 2 ** 31:
            x -= 2 ** 32
        return x
