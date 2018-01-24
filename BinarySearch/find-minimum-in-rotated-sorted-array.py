"""
Find Minimum in Rotated Sorted Array
@ Binary Search
@ Corner case: array is absolute ascending.
@ SolutionV2: take nums[-1] instead of nums[0] as pivot, this will release us from corner case.
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if nums[-1] >= nums[0]:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (right - left) / 2 + left
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] >= nums[0]:
                left = mid
            else:
                right = mid
        print left, right
        return min(nums[left], nums[right])
