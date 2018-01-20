"""
Fraction to Recurring Decimal
@ Math + Hash: 1. a math problem apparently.
               2. how to know the fractional part is repeating? --> hashMap map numerator to index to insert '('
@ Note for a math problem: 1. negative numbers
                           2. zero (zero as divisor!!!)
                           3. overflow
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not denominator:
            return ""
        if not numerator:
            return "0"
        # 1. check negative
        negFlag = (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0)
        numerator, denominator = abs(numerator), abs(denominator)
        res = ["-"] if negFlag else []
        # 2. get integral part
        res.append(str(numerator / denominator))
        numerator %= denominator
        if not numerator:
            return "".join(res)
        # 3. get fractional part(attention to repeating part)
        res.append(".")
        num2ind = {numerator: len(res)}  # ind is where to insert '('
        while numerator:
            numerator *= 10
            res.append(str(numerator / denominator))
            numerator %= denominator
            if numerator in num2ind:
                res.insert(num2ind[numerator], '(')
                res.append(')')
                break
            num2ind[numerator] = len(res)
        return "".join(res)
