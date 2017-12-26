"""
Different Ways to Add Parentheses
@ Divide And Conquer
"""


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if not input:
            return []
        results = []
        for i in range(len(input)):
            if input[i] in ['+', '-', '*']:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        results.append(self.calcu(l, input[i], r))
        return results if results else [int(input)]

    def calcu(self, oper1, operator, oper2):
        if operator == '+':
            return oper1 + oper2
        if operator == '-':
            return oper1 - oper2
        if operator == '*':
            return oper1 * oper2

