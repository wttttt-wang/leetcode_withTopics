"""
Move Zeroes
@ Two pointers
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[left] = nums[r]
                left += 1
        for i in range(left, len(nums)):
            nums[i] = 0

