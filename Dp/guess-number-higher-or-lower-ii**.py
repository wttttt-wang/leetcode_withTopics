"""
Guess Number Higher or Lower II
@ dp + MinMax: 1. when there are 1 number, cost = 0
               2. when there are 2 numbers: i, i + 1. then minCost = i
               3. when there are 3 numbers: i - 1, i, i + 1, then minCost = i
              So, when there are multiple numbers from i to j, we divide it:
                  dp[i][j] = min(k, max(dp[i][k - 1], dp[k + 1][j])).
                  This is where 'MinMax' goes. --> Minimum cost with considering all (worst) situation.
"""


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        # dp[i][j] = min(k + max(dp[i][k - 1], dp[k + 1][j])), dp[i][i] = 0, dp[i][i + 1] = i, res = dp[1][n]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n, 0, -1):
            dp[i][i] = 0
            for j in range(i + 1, n + 1):
                tmp = sys.maxint
                for k in range(i, j + 1):
                    tmp = min(tmp, k + max(dp[i][k - 1] if k > i else 0, dp[k + 1][j] if k < j else 0))
                dp[i][j] = tmp
        return dp[1][n]
