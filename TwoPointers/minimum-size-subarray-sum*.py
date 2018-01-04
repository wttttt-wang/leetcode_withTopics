"""
Minimum Size Subarray Sum
@ Two pointers
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left, right = 0, 0
        res, sum = sys.maxint, 0
        for r in range(len(nums)):
            sum += nums[r]
            if sum >= s:
                while sum >= s and left <= r:
                    sum -= nums[left]
                    left += 1
                res = min(res, r - left + 2)
        return res if res != sys.maxint else 0

