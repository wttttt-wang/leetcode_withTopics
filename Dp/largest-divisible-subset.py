"""
Largest Divisible Subset
@ sort + dp: The key point is sort then we can use dp.
             O(N ^ 2) time & O(N) space
"""


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        # dp[i] = max(dp[j]) + 1 where nums[i] % nums[j] == 0, dp[0] = 1
        dp, prevInd, maxVal, maxInd = [1] * len(nums), [i for i in range(len(nums))], 1, 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prevInd[i] = j
            if dp[i] > maxVal:
                maxVal = dp[i]
                maxInd = i
        res = []
        while True:
            res.append(nums[maxInd])
            if prevInd[maxInd] == maxInd:
                break
            maxInd = prevInd[maxInd]
        return res
