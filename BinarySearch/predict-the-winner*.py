"""
Predict the Winner
@ dp: dp[i][j] stands for the value the 'current' first one can win more than the second one.
"""


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        # dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        dp = [[0] * len(nums) for _ in range(2)]
        for i in range(len(nums) - 1, -1, -1):
            dp[i % 2][i] = nums[i]
            for j in range(i + 1, len(nums)):
                dp[i % 2][j] = max(nums[i] - dp[(i + 1) % 2][j], nums[j] - dp[i % 2][j - 1])
        return dp[0][len(nums) - 1] >= 0
