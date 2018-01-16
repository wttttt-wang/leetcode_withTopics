"""
Burst Balloons
@ Dp + Divide&Conquer
"""


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # dp[i][j] = max(dp[i][k - 1] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1])
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums) - 2, 0, -1):
            dp[i][i] = nums[i] * nums[i - 1] * nums[i + 1]
            for j in range(i + 1, len(nums) - 1):
                dp[i][j] = -sys.maxint
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1])
        return dp[1][len(nums) - 2]
