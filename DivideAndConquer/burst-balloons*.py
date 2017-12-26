"""
Burst Balloons
@ Divide And Conquer: Divide into individual sub-problems by considering each position be to the last to be bursted.
"""
import sys


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # fill
        nums.insert(0, 1)
        nums.append(1)
        # dp[i][j] = max(dp[i][k - 1] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1])
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums) - 2, 0, -1):
            for j in range(i, len(nums) - 1):
                tmpMax = -sys.maxint
                for k in range(i, j + 1):
                    tmpMax = max(tmpMax, dp[i][k - 1] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1])
                dp[i][j] = tmpMax
        return dp[1][len(nums) - 2]


so = Solution()
print so.maxCoins([3,1,5,8])
