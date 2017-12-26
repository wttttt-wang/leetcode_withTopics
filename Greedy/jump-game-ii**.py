"""
Jump Game II
@ Greedy: The key point is pay attention to the current(current jump number) max pos that can jump to.
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res, end, nextInd = 0, 0, 0
        for i in range(len(nums) - 1):
            nextInd = max(nextInd, i + nums[i])
            if i == end:
                res += 1
                end = nextInd
                if end >= len(nums) - 1:
                    break
        return res
