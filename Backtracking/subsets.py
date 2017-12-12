"""
Subsets
@ Backtracking
@ can without sort
@ Also see 'BitManipulation/Subsets.py'
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.helper(nums, [], results, 0)
        return results

    def helper(self, nums, result, results, startInd):
        results.append(result[:])
        for i in range(startInd, len(nums)):
            result.append(nums[i])
            self.helper(nums, result, results, i + 1)
            result.pop()
