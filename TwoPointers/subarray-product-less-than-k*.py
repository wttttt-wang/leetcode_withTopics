"""
Subarray Product Less Than K
@ Two pointers
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        left, right, product, res = 0, 0, 1, 0
        while right < len(nums):
            product *= nums[right]
            while left <= right and product >= k:
                product /= nums[left]
                left += 1
            res += (right - left + 1)
            right += 1
        return res
