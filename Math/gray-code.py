"""
Gray Code
@ Math: G(i) = i ^ (i/2)
@ Also see: 'backtracking/gray-code' (recommended)
"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 0:
            return [0]
        results = []
        for i in range(1 << n):
            results.append(i ^ i >> 1)
        return results
