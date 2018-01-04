"""
Ugly Number II
@ DP: O(N * k) time
@ Note: Pay attention to remove duplicates!!!
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return None
        inds, base = [0, 0, 0], [2, 3, 5]
        dp = [1] * n
        for i in range(1, n):
            dp[i] = min([dp[inds[j]] * base[j] for j in range(len(base))])
            for j in range(len(base)):
                if dp[inds[j]] * base[j] == dp[i]:
                    inds[j] += 1
        return dp[-1]
