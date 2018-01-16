"""
Triangle
@ dp
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        # dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        dp = [[0] * len(triangle) for _ in range(2)]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j] if j < i else sys.maxint, dp[(i - 1) % 2][j - 1] if j > 0 else sys.maxint) + triangle[i][j]
        return min(dp[(len(triangle) - 1) % 2])
