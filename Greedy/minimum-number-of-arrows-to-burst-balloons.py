"""
Minimum Number of Arrows to Burst Balloons
@ Greedy: Almost the same as 'Greedy/non-overlapping-intervals'
"""


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        res, right = 0, points[0][0] - 1
        for s, e in points:
            if s > right:
                res += 1
                right = e
        return res

