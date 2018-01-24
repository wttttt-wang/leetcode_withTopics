"""
Partition Equal Subset Sum
@ Dp + Hash: This is a 0/1 knapsack problem: for each number, we can pick it or not. And the target is to sum to target.
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or sum(nums) % 2:
            return False
        target = sum(nums) / 2
        occurs = {0}
        for val in nums:
            if target - val in occurs:
                return True
            tmpSet = set()
            for key in occurs:
                tmpSet.add(key + val)
            occurs |= tmpSet
        return False
