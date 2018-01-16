"""
Maximal Square
@ dp: Not the same as 'Stack/MonotoneStack/maximal-rectangle' at all
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        # dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if matrix[i][j] == 1 else 0 (side length)
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = 1 if matrix[0][0] == '1' else 0
        res = dp[0][0]
        for j in range(1, n):
            dp[0][j] = 1 if matrix[0][j] == '1' else 0
            res = max(res, dp[0][j])
        for i in range(1, m):
            dp[i % 2][0] = 1 if matrix[i][0] == '1' else 0
            res = max(res, dp[i % 2][0])
            for j in range(1, n):
                dp[i % 2][j] = min(dp[i % 2][j - 1], dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - 1]) + 1 if matrix[i][j] == '1' else 0
                res = max(res, dp[i % 2][j])
        return res * res
