"""
Count Numbers with Unique Digits
@ Math: Combination.  for numbers with 1 digit there are 10 different numbers, for numbers with 2 digits there are 9 * 9
                      3 --> 9 * 9 * 8, 4 --> 9 * 9 * 8 * 7, ..., 10 --> 9 * 9 * 8 * ... * 1, 11 --> 0, 12 --> 0,...
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
        if n >= 10:
            n = 10
        res = 0  # a problem of combination
        for i in range(n, 0, -1):
            if i == 1:
                res += 10
            elif i == 2:
                res += 81
            else:
                tmpRes, tmp = 9, 9
                while tmp + i >= 11:
                    tmpRes *= tmp
                    tmp -= 1
                res += tmpRes
        return res
