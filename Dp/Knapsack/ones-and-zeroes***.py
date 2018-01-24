"""
Ones and Zeroes
@ Dp (KnapSack problem): For each element with two choices: select or not.
@ Attention: From iterate form right-bottom to left-top!!!
"""


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        if not strs:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            cnt1, cnt0 = self.cnt01(s)
            for i in range(m, cnt0 - 1, -1):
                for j in range(n, cnt1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - cnt0][j - cnt1] + 1)
        return dp[m][n]

    def cnt01(self, s):
        cnt1, cnt0 = 0, 0
        for c in s:
            if c == '1':
                cnt1 += 1
            else:
                cnt0 += 1
        return cnt1, cnt0
