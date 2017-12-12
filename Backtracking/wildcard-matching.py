"""
Wildcard Matching
@ dp
@ Tricky: dp[i][j] = dp[i - 1][j] or dp[i][j - 1] when p[i - 1] == '*'
          like regular-expression-matching  --> only to consider '*' matching 0 or non-zero characters currently.
@ Optimization: see greedy/wildcard-matching
@ Time: O(P * (S ^ 2))
@ Space: O(P * S)
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        dp = [[False] * (len(s) + 1) for _ in range(2)]
        dp[0][0] = True
        # 1. initialization
        for i in range(1, len(p) + 1):
            dp[i % 2][0] = p[i - 1] == '*' and dp[(i - 1) % 2][0]
            for j in range(1, len(s) + 1):
                if p[i - 1] == '*':
                    dp[i % 2][j] = dp[(i - 1) % 2][j] or dp[i % 2][j - 1]
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1] and (p[i - 1] == '?' or p[i - 1] == s[j - 1])
        return dp[len(p) % 2][-1]

