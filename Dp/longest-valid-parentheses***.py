"""
Longest Valid Parentheses
@ dp: dp[i] stores the longest valid parentheses ends at index i. O(N) time & space
@ Note: Always check index >= 0 before get value of it.
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) < 2:
            return 0
        dp, res = [0] * len(s), 0   # dp[i] stores the longest valid parentheses ends at index i
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                    res = max(res, dp[i])
                else:
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        # Attention: Do not forget dp[i - dp[i - 1] - 2]
                        dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
                        res = max(res, dp[i])
        return res
