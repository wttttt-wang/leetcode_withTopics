"""
Bitwise AND of Numbers Range
@ Bit Manipulation: Ummmm... I thought I came up with a nice solution with O(1) time(See solutionV1).
                    But there are more concise way in fact TAT(See solutionV2 & V3).
                    The key point is that res is the left common part of m and n.
                    SolutionV3 is really amazing. > < (Note the way it pick the left common part of two integers.)
"""


class SolutionV3(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            return 0
        moveFactor = 1
        while m != n:  # loop until the left part is equal for m and n
            m >>= 1
            n >>= 1
            moveFactor <<= 1
        return m * moveFactor


class SolutionV2(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            return 0
        res = 0
        for i in range(31, -1, -1):
            v1, v2 = (m >> i) & 1, (n >> i) & 1
            if v1 and v2:
                res += (1 << i)
            elif v1 != v2:
                return res
        return res


class SolutionV1(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            return 0
        res, base, x = 0, 2, n - m + 1
        for i in range(32):
            val = 0
            if x <= base / 2 and base / 2 <= m % base <= base - x:
                val = 1
            base *= 2
            if val:
                res += (val << i)
        return res


so = SolutionV3()
print so.rangeBitwiseAnd(4, 7)
