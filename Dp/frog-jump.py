"""
Frog Jump
@ Dp + Hash: Not typical dp.
"""


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if not stones:
            return False
        jumps = {0: [1]}
        TRANS = [-1, 0, 1]
        for i in range(1, len(stones) - 1):
            jumps[stones[i]] = set()
        for i in range(len(stones) - 1):
            for key in jumps[stones[i]]:
                nextInd = key + stones[i]
                if nextInd == stones[-1]:
                    return True
                if nextInd in jumps:
                    for t in TRANS:
                        if key + t > 0:
                            jumps[nextInd].add(key + t)
        return False

