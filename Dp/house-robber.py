"""
House Robber
@ dp
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]), dp[0] = nums[0]
        dp = [nums[0], 0, 0]
        for i in range(len(nums)):
            dp[i % 3] = max(dp[(i - 1) % 3], dp[(i - 2) % 3] + nums[i])
        return dp[(len(nums) - 1) % 3]
