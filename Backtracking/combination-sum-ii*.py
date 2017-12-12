"""
Combination Sum II
@ Attention: Please pay attention to how to remove duplicates!!!
             The point is: for current round, always select the first one of the duplicate(continuous) numbers.
                           For current round means 'i > startInd'
@ Backtracking
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = []
        self.helper(candidates, target, [], results, 0)
        return results

    def helper(self, candidates, target, result, results, startInd):
        if target == 0:
            results.append(result[:])
        if target <= 0:
            return
        for i in range(startInd, len(candidates)):
            if i > startInd and candidates[i] == candidates[i - 1]:  # This is important
                continue
            result.append(candidates[i])
            self.helper(candidates, target - candidates[i], result, results, i + 1)
            result.pop()
