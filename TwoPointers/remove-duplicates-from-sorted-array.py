"""
Remove Duplicates from Sorted Array
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
        left = 0
        for r in range(1, len(nums)):
            if nums[r] != nums[left]:
                left += 1
                nums[left] = nums[r]
        return left + 1

