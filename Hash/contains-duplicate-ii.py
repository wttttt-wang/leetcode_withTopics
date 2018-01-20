"""
Contains Duplicate II
@ Hash
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        occurs = {}
        for i in range(len(nums)):
            if nums[i] in occurs and i - occurs[nums[i]] <= k:
                return True
            occurs[nums[i]] = i  # store the right-most ind
        return False
