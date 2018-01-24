"""
Find Peak Element
@ Binary Search: 1. num[-1] = num[n] = -INF can make sure the peak element exists.
                 2. Then we can draw the model.
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (right - left) / 2 + left
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid - 1] < nums[mid]:
                left = mid
            else:
                right = mid
        return left if nums[left] > nums[right] else right
