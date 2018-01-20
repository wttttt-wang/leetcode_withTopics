"""
Split Array Largest Sum
@ dp: O(m * N * N) time, O(m * N) space
"""


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if not nums:
            return 0
        # dp[i][k] = min(max(dp[j][k - 1], sum(nums[j + 1: i + 1]))), dp[i][1] = sum(nums[:i + 1])
        dp = [[0] * (m + 1) for _ in range(len(nums))]
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][1] = dp[i - 1][1] + nums[i]
        for i in range(len(nums)):
            for k in range(2, m + 1):
                tmpVal, tmpSum = sys.maxint, nums[i]
                for j in range(i - 1, -1, -1):
                    tmpVal = min(tmpVal, max(dp[j][k - 1], tmpSum))
                    tmpSum += nums[j]
                dp[i][k] = tmpVal
        return dp[len(nums) - 1][m]
