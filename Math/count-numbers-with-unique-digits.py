"""
Count Numbers with Unique Digits
@ Math
"""


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        if n == 0:
            return 1
        res, base, proBase = 0, 81, 9
        for i in range(1, min(n + 1, 11)):
            if i == 1:
                res += 10
            else:
                res += base
                proBase -= 1
                base *= proBase
        return res
