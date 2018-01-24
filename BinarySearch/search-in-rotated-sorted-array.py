"""
Search in Rotated Sorted Array
@ Binary Search: First we try to draw the line model. And the key point is compare with nums[0].
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (right - left) / 2 + left
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target < nums[0]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        return right if nums[right] == target else -1

