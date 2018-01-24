"""
Brick Wall
@ Hash: The key point is to find the most frequent prefix-sum.
"""


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if not wall:
            return 0
        occurs, res = {}, 0
        for w in wall:
            pre = 0
            for i in range(len(w) - 1):
                pre += w[i]
                occurs[pre] = occurs.get(pre, 0) + 1
                res = max(res, occurs[pre])
        return len(wall) - res
