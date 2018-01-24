"""
Search Insert Position
@ Binary Search
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        # bs: to find the left-most value that >= target
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (right - left) / 2 + left
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] >= target:
            return left
        if nums[right] >= target:
            return right
        return right + 1
