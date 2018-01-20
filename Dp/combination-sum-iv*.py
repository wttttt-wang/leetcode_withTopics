"""
Combination Sum IV
@ dp
@ Follow up: If there are negative numbers, then dp[i] <--> dp[i + j] with has interactions,
             i.e. dp[i] may affect dp[i + j] and also dp[i + j] may affect dp[i].
             Then there are may be infinite solutions.
             Limitation should be added:
                  each number can only be used once, or either positive or negative number should be used only one time.
             Solution updated: should use memorization instead of dp.
"""


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1  # dp[i] = sum(dp[i - val]) where val in nums
        for i in range(1, target + 1):
            for val in nums:
                if i - val >= 0:
                    dp[i] += dp[i - val]
        return dp[target]
