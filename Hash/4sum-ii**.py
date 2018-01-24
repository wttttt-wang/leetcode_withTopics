"""
4Sum II
@ Hash(Or Binary Search): This is easy indeed, but ummm....
                          The key point is to cut A, B, C, D to two pairs.
"""


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        if not A:
            return 0
        res, occurs = 0, {}
        for v1 in A:
            for v2 in B:
                occurs[v1 + v2] = occurs.get(v1 + v2, 0) + 1
        for v1 in C:
            for v2 in D:
                res += occurs.get(-v1 - v2, 0)
        return res
