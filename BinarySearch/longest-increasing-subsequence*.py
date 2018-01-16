"""
Longest Increasing Subsequence
@ Binary search
@ Note: please pay attention to '=' when binary search.
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tmpArr = []
        for val in nums:
            self.bs_insert(val, tmpArr)
        return len(tmpArr)

    def bs_insert(self, val, nums):
        # find left most ind where nums[ind] > val, and replace
        if not nums:
            nums.append(val)
            return
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (right - left) / 2 + left
            if nums[mid] >= val:
                right = mid
            else:
                left = mid
        if nums[left] >= val:
            nums[left] = val
        elif nums[right] >= val:
            nums[right] = val
        else:
            nums.append(val)
