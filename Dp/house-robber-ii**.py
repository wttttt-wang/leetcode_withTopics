"""
House Robber II
@ Dp: The solution is really tricky: by considering select first one or last one separately.
@ Corner Case: len(nums) == 1 !!!
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        res = self.helper(nums, 0, len(nums) - 1)
        res = max(res, self.helper(nums, 1, len(nums)))
        return res

    def helper(self, nums, s, e):
        dp = [0, 0, 0]
        for i in range(s, e):
            dp[i % 3] = max(dp[(i - 1) % 3], dp[(i - 2) % 3] + nums[i])
        return dp[(e - 1) % 3]
