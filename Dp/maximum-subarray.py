"""
Maximum Subarray
@ Dp
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -sys.maxint
        sumVal = 0
        for n in nums:
            sumVal += n
            res = max(res, sumVal)
            if sumVal < 0:
                sumVal = 0
        return res
