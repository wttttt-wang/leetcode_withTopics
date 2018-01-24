"""
Divide Two Integers
@ Dp + Binary Search + Bit Manipulation: The solution below is amazing!!!
@ 1. a / b = x --> a - bx < x. So the basic solution is to subtract b in each round. O(x) time.
  2. How to improve? --> Each round we subtract val successfully, we update val to 2 * val(val << 1).
                         Then if left >= val, then subtract, else we shrink val.
@ Note: For math problem, always consider negative numbers & 0 & overflow.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not divisor or not dividend:
            return 0
        negFlag = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        val, base, res = divisor, 1, 0
        while dividend >= divisor:
            if dividend >= val:
                dividend -= val
                res += base
                base <<= 1
                val <<= 1
            else:
                base >>= 1
                val >>= 1
        res = -res if negFlag else res
        if res > 2147483647:
            res = 2147483647
        elif res < -2147483648:
            res = -2147483648
        return res
