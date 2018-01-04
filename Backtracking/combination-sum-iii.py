"""
Combination Sum III
@ Backtracking: Nothing special
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k < 0 or n < 0:
            return []
        results = []
        self.helper(1, k, [], results, n)
        return results

    def helper(self, start, k, result, results, left_target):
        if len(result) == k:
            if left_target == 0:
                results.append(result[:])
            return
        if left_target <= 0:
            return
        for i in range(start, 10):
            result.append(i)
            self.helper(i + 1, k, result, results, left_target - i)
            result.pop()
