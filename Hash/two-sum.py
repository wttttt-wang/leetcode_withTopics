"""
Two Sum
@ Hash table
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        inds = {}
        for i in range(len(nums)):
            if target - nums[i] in inds:
                return [inds[target - nums[i]], i]
            inds[nums[i]] = i
        return []
