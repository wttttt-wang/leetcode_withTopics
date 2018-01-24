"""
Search for a Range
@ Binary Search
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        # 1. find the left-most target
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (right - left) / 2 + left
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if target == nums[left]:
            ind1 = left
        elif target == nums[right]:
            ind1 = right
        else:
            return [-1, -1]
        # 2. find the right-most target (can start from ind1)
        left, right = ind1, len(nums) - 1
        while left < right - 1:
            mid = (right - left) / 2 + left
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        ind2 = right if nums[right] == target else left
        return [ind1, ind2]
