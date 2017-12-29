"""
Decode String
@ Stack
@ Note: s = "1[" + s + "]" to get the final result  (eg: "3[a2[c]]")
"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        s = "1[" + s + "]"   # Attention here!!!
        stack, curr, number = [], "", 0
        for v in s:
            if v == '[':
                if curr:
                    stack.append(curr)
                    curr = ""
                stack.append(number)
                number = 0
            elif v == ']':
                n = stack.pop()
                t = curr
                for i in range(n - 1):
                    curr += t
                if stack and not isinstance(stack[-1], int):   # Attention: not forget.
                    tmp = stack.pop()
                    tmp += curr
                    curr = tmp
                number = 0
            elif v.isdigit():
                number = number * 10 + int(v)
            else:
                curr += v
        return curr

