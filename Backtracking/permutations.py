"""
Permutations
@ Basic Backtracking
@ Tricky: exchange instead of using visited array
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        self.helper(nums, [], results, 0)
        return results

    def helper(self, nums, result, results, startInd):
        if startInd == len(nums):
            results.append(result[:])
            return
        for i in range(startInd, len(nums)):
            result.append(nums[i])
            nums[i], nums[startInd] = nums[startInd], nums[i]  # exchange instead of using visited array
            self.helper(nums, result, results, startInd + 1)
            nums[startInd], nums[i] = nums[i], nums[startInd]
            result.pop()

