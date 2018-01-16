"""
Dungeon Game
@ dp: The key point is the way of updating dp[i][j] for that dp[i][j] will not < 0. But will = 0.
"""


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 0
        # dp[i][j] = max(0, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]), from bottom-right to upper-left
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(2)]
        dp[(m - 1) % 2][n - 1] = 1 - (0 if dungeon[-1][-1] >= 0 else dungeon[-1][-1])
        for j in range(n - 2, -1, -1):
            val = dp[(m - 1) % 2][j + 1] - dungeon[m - 1][j]
            dp[(m - 1) % 2][j] = val if val > 0 else 1
        for i in range(m - 2, -1, -1):
            val = dp[(i + 1) % 2][-1] - dungeon[i][-1]
            dp[i % 2][-1] = val if val > 0 else 1
            for j in range(n - 2, -1, -1):
                val = min(dp[(i + 1) % 2][j], dp[i % 2][j + 1]) - dungeon[i][j]
                dp[i % 2][j] = val if val > 0 else 1
        return dp[0][0]

