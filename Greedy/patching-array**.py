"""
Patching Array
@ Greedy: when current cover is [0, upper) if nums[ind] <= upper, then the cover becomes [0, upper + nums[ind]]
                                           else new element needed to be inserted.  (This is really tricky)
"""


class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        upper, res, ind = 1, 0, 0
        while upper <= n:
            if ind < len(nums) and nums[ind] <= upper:
                upper += nums[ind]
                ind += 1
            else:
                res += 1
                upper *= 2
        return res
