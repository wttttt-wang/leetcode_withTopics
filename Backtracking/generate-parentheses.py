"""
Generate Parentheses
@ Backtracking
@ Explanation: For a valid expression with parentheses, for each sub-prefix must satisfy
               "number of left parentheses >= number of right parentheses"
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        results = []
        self.helper(n, 0, 0, [], results)
        return results

    def helper(self, n, left, right, result, results):
        if left == n and right == n:
            results.append("".join(result))
            return
        # case1: add '('
        if left < n:
            result.append('(')
            self.helper(n, left + 1, right, result, results)
            result.pop()
        # case2: add ')' --> only if right < n and right < left
        if right < n and right < left:
            result.append(')')
            self.helper(n, left, right + 1, result, results)
            result.pop()
