"""
Sort Colors
@ Two pointers
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        left, right = 0, len(nums) - 1
        ind = 0
        while ind <= right:
            if nums[ind] == 0:
                nums[left], nums[ind] = nums[ind], nums[left]
                left += 1
                ind += 1
            elif nums[ind] == 2:
                nums[right], nums[ind] = nums[ind], nums[right]
                right -= 1
            else:
                ind += 1

