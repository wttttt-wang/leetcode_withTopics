"""
Edit Distance
@ dp: dp[i][j] = min(dp[i - 1][j - 1] + (0 if w1[i - 1] == w2[j - 1] else 1) , dp[i - 1][j] + 1, dp[i][j - 1] + 1)
@ Note that dp[i][j] is associated with word1[i - 1] and word2[j - 1]
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1), [0] * (n + 1)]
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            dp[i % 2][0] = i
            for j in range(1, n + 1):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1),
                                   dp[(i - 1) % 2][j] + 1, dp[i % 2][j - 1] + 1)
        return dp[len(word1) % 2][-1]
