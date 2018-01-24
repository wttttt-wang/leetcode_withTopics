"""
Arithmetic Slices II - Subsequence
@ dp
"""


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) < 3:
            return 0
        dp, res = [{} for _ in range(len(A))], 0
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    res += dp[j][diff]
                    dp[i][diff] = dp[i].get(diff, 0) + dp[j][diff] + 1
                else:
                    dp[i][diff] = dp[i].get(diff, 0) + 1
        return res
