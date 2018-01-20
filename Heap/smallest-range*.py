"""
Smallest Range
@ heap: The key point is for current window, the only way to get a smaller window is to move right the leftmost ind.
"""


from heapq import *


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return []
        res, heap, inds = None, [], [1] * len(nums)
        curMax = -sys.maxint  # use curMax is really tricky
        for i in range(len(nums)):
            if nums[i]:
                heappush(heap, (nums[i][0], i))
                curMax = max(curMax, nums[i][0])
        while len(heap) == len(nums):
            val, ind = heappop(heap)
            if not res or curMax - val < res[1] - res[0]:
                res = (val, curMax)
            if inds[ind] < len(nums[ind]):
                curMax = max(curMax, nums[ind][inds[ind]])
                heappush(heap, (nums[ind][inds[ind]], ind))
                inds[ind] += 1
        return res
