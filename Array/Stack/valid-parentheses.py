"""
Valid Parentheses
@ Stack
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        for v in s:
            if v == '(' or v == '[' or v == '{':
                stack.append(v)
            elif v == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif v == ']':
                if not stack or stack.pop() != '[':
                    return False
            else:
                if not stack or stack.pop() != '{':
                    return False
        return True if not stack else False


