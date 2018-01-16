"""
Decode Ways
@ dp
@ Note that the solution itself is not difficult. The key point are the corner cases:
  1. '0' can not be as starter(no leading zeros are permitted.) or a single value.
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        # dp: dp[i] = dp[i - 1] + dp[i - 2] if int(s[i - 1: i + 1]) <= 26 else 0
        dp = [0, 0, 0]
        dp[0] = 1
        for i in range(1, len(s) + 1):
            dp[i % 3] = (dp[(i - 1) % 3] if s[i - 1] != '0' else 0) + \
                        (dp[(i - 2) % 3] if (i >= 2 and s[i - 2] != '0' and int(s[i - 2: i]) <= 26) else 0)
        return dp[len(s) % 3]
