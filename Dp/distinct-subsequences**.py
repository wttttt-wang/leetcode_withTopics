"""
Distinct Subsequences
@ dp: The solution with O(N ^ 3) time is trivial. Try to solve it with O(N ^ 2) time.
      Always think of globalDp & localDp
      For this problem, dp[i][j] stands for a global value.
"""


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s:
            return 0
        if not t:
            return 1
        # dp, dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - 1] if s[i - 1] == t[j - 1] else 0) --> not match & match (if can)
        dp = [[0] * (len(t) + 1) for _ in range(2)]
        dp[0][0] = 1  # dp[0][j] = 0 when j > 0
        for i in range(1, len(s) + 1):
            dp[i % 2][0] = dp[(i - 1) % 2][0]
            for j in range(1, len(t) + 1):
                dp[i % 2][j] = dp[(i - 1) % 2][j] + (dp[(i - 1) % 2][j - 1] if s[i - 1] == t[j - 1] else 0)
        return dp[len(s) % 2][-1]
