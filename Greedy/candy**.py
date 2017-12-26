"""
Candy
@ Greedy + Backward-Forward traverse
@ O(N) time & O(N) space
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        left = []
        for i in range(len(ratings)):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left.append(left[-1] + 1)
            else:
                left.append(1)
        rightTmp, res = 0, 0
        for i in range(len(ratings) - 1, -1, -1):
            if i < len(ratings) - 1 and ratings[i] > ratings[i + 1]:
                rightTmp += 1
            else:
                rightTmp = 1
            res += max(rightTmp, left[i])
        return res
