"""
Remove Duplicates from Sorted Array II
@ Two pointers
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return len(nums)
        left = 1
        for r in range(2, len(nums)):
            if nums[r] != nums[left] or nums[r] != nums[left - 1]:
                nums[left + 1] = nums[r]
                left += 1
        return left + 1

