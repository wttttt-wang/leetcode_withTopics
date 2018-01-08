"""
Regular Expression Matching
@ dp
@ Note: Be careful when initializing
@ Recommend to solve this problem using backtracking. See 'Backtracking/regular-expression-matching'
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
        for i in range(1, len(p) + 1):
            dp[i % 2][0] = dp[(i - 2) % 2][0] if p[i - 1] == '*' else False   # initialization
            for j in range(1, len(s) + 1):
                if p[i - 1] == '*':
                    if dp[(i - 2) % 2][j]:
                        dp[i % 2][j] = True
                        continue
                    if (p[i - 2] == '.' or p[i - 2] == s[j - 1]) and dp[i % 2][j - 1]:
                        dp[i % 2][j] = True
                        continue
                elif (p[i - 1] == '.' or p[i - 1] == s[j - 1]) and dp[(i - 1) % 2][j - 1]:
                    dp[i % 2][j] = True
                    continue
                dp[i % 2][j] = False
        return dp[len(p) % 2][-1]
