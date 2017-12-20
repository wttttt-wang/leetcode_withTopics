"""
Gray Code
@ Backtracking: Get results[n = 3] from results[n = 2] : [00, 01, 11, 10] --> [000, 001, 011, 010, 110, 111, 101, 100]
@ Also see: 'math/gray-code'
"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 0:
            return []
        results = [0]
        added = 1
        for i in range(n):
            results += [added + results[j] for j in range(len(results) - 1, -1, -1)]
            added <<= 1
        return results
