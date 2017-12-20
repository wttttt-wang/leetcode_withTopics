"""
Subsets II
@ Backtracking
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        results = []
        self.helper(nums, [], results, 0)
        return results

    def helper(self, nums, result, results, startInd):
        results.append(result[:])
        for i in range(startInd, len(nums)):
            if i > startInd and nums[i] == nums[i - 1]:
                continue
            result.append(nums[i])
            self.helper(nums, result, results, i + 1)
            result.pop()
