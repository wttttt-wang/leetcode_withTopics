"""
Maximum Product Subarray
@ dp
@ Cases: 1. curr < 0; 2. curr > 0; 3. curr = 0 (val == 0)
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minPos, maxNeg = 1, 1
        res, curr = -sys.maxint, 1
        for val in nums:
            if not val:
                res = max(res, 0)
                minPos, maxNeg, curr = 1, 1, 1
            else:
                curr *= val   # curr will never be zero
                res = max(res, curr / minPos, curr / maxNeg)
                if curr > 0:
                    minPos = min(minPos, curr)
                else:
                    maxNeg = max(maxNeg, curr) if maxNeg < 0 else curr
        return res
