"""
Missing Number
@ Bit Manipulation: SolutionV1: Using xor
                    SolutionV2: Using sum
"""


class SolutionV1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for val in nums:
            res ^= val
        for i in range(len(nums) + 1):
            res ^= i
        return res


class SolutionV2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums) * (len(nums) + 1) / 2
        for val in nums:
            res -= val
        return res
