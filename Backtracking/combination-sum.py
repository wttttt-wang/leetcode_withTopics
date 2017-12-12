"""
Combination Sum
@ Backtracking
@ Attention: Without duplicates does not mean 'there are no duplicates in results'.
             But 'without duplicates' --> no need for sorting
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        # candidates.sort()
        self.helper(candidates, target, [], results, 0)
        return results

    def helper(self, candidates, target, result, results, startInd):
        if target == 0:
            results.append(result[:])
            return
        if target < 0:
            return
        for i in range(startInd, len(candidates)):
            result.append(candidates[i])
            self.helper(candidates, target - candidates[i], result, results, i)
            result.pop()
