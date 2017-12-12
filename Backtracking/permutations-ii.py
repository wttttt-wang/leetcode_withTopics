"""
Permutations II
@ Backtracking
@ Notice: Key of point of this type of problems is how to remove duplicates.
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.helper(nums, [], results, [False] * len(nums))
        return results

    def helper(self, nums, result, results, visited):
        if len(result) == len(nums):
            results.append(result[:])
            return
        for i in range(len(nums)):
            if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                # can not visited it if the former same one not visited
                continue
            result.append(nums[i])
            visited[i] = True
            self.helper(nums, result, results, visited)
            result.pop()
            visited[i] = False

