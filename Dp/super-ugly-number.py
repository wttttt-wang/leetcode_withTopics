"""
Super Ugly Number
@ Dp: extension of 'dp/ugly-number-ii', nothing special.
"""


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        inds = [0] * len(primes)
        dp = [1] * n
        for i in range(1, n):
            dp[i] = min([dp[inds[x]] * primes[x] for x in range(len(primes))])
            for j in range(len(primes)):
                if dp[inds[j]] * primes[j] == dp[i]:
                    inds[j] += 1   # Attention: remove duplicates
        return dp[-1]
