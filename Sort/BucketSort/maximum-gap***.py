"""
Maximum Gap
@ Bucket Sort: The basic thought is for an array with [minVal, maxVal] with length n,
               the maximum gap will not be smaller than (maxVal - minVal) / n - 1 (Equal is possible).
               So, we can only split the array into buckets, with each bucket accommodate val between [a, b)
               where b - a == (maxVal - minVal) / n - 1 (i.e. bucket size is the minimum possible answer - 1)
@ Note: There are many division, please pay much attention to the dividend
        !!! IT CAN NOT BE ZERO!!!
"""


import sys


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0
        minVal, maxVal = sys.maxint, -sys.maxint
        for val in nums:
            minVal, maxVal = min(minVal, val), max(maxVal, val)
        if minVal == maxVal:
            return 0  # Attention: This is important!!! For checking zero division!!!
        gap = (maxVal - minVal) / (len(nums) - 1) + (1 if (maxVal - minVal) % (len(nums) - 1) else 0)
        gapNum = (maxVal - minVal + 1) / gap + (1 if (maxVal - minVal + 1) % gap else 0)
        buckets = [None] * gapNum

        # update buckets
        for val in nums:
            ind = (val - minVal) / gap
            if not buckets[ind]:
                buckets[ind] = [val, val]
            else:
                buckets[ind][0] = min(val, buckets[ind][0])
                buckets[ind][1] = max(val, buckets[ind][1])
        # update res
        res, prevMax = gap, sys.maxint
        for i in range(len(buckets)):
            if buckets[i]:
                res = max(res, buckets[i][0] - prevMax)
                prevMax = buckets[i][1]
        return res
