"""
Arithmetic Slices
@ Math: The solution is really amazing!!! No more explanation, code talks!
"""


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) < 3:
            return 0
        res, cur = 0, 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                cur += 1
                res += cur
            else:
                cur = 0
        return res
