"""
Simplify Path
@ Stack
@ Corner case: 1. /../
               2. redundant slashes like '/home//foo' --> '/home/foo'
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ""
        stack = []
        elements = path.split('/')
        for ele in elements:
            if not ele or ele == '.':
                continue
            if ele == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(ele)
        return '/' + "/".join(stack)


