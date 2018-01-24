"""
Target Sum
@ dp
"""


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        before = {0: 1}
        up = sum(nums)
        down = -up
        for val in nums:
            dp = {}
            for t in before:
                if down <= t + val <= up:
                    dp[t + val] = dp.get(t + val, 0) + before[t]
                if down <= t - val <= up:
                    dp[t - val] = dp.get(t - val, 0) + before[t]
            before = dp
        return before.get(S, 0)
