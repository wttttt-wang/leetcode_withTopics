"""
Subsets
@ Bit Manipulation
@ For each index: we can choose to add this number or not. So this becomes a bit manipulation problem.
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        for i in range(1 << len(nums)):
            result = []
            for j in range(len(nums)):
                if i & (1 << j):
                    result.append(nums[j])
            results.append(result)
        return results
