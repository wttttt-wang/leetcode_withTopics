"""
Unique Paths
@ dp
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                dp[i][j] += ((dp[i - 1][j] if i > 0 else 0) + (dp[i][j - 1] if j > 0 else 0))
        return dp[-1][-1]
