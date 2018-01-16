"""
Longest Valid Parentheses
@ Stack: The key point is pop the valid parentheses out, leave the invalid index in stack.
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) < 2:
            return 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or not stack or s[stack[-1]] == ')':
                stack.append(i)
            else:
                stack.pop()
        a, b, res = len(s), 0, 0
        while stack:
            b = stack.pop()
            res = max(res, a - b - 1)
            a = b
        return max(res, a)

