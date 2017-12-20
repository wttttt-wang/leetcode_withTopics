"""
Remove Element
@ Two Pointers
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        left = -1
        for r in range(len(nums)):
            if nums[r] != val:
                left += 1
                nums[left] = nums[r]
        return left + 1
