"""
range-sum-query-immutable
@ dp + prefix sum
"""


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0]
        self.len = len(nums)
        for val in nums:
            self.dp.append(val + self.dp[-1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0:
            i = 0
        if j >= self.len:
            j = self.len - 1
        return self.dp[j + 1] - self.dp[i]
