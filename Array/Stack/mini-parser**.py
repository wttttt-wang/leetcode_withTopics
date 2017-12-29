"""
Mini Parser
@ Stack
@ Corner case: 1. "[]" vs "[0]"   2. "12" or "-123" (single number not list)
@ Note: we need 'l' to record the start ind of an number to take care of empty number
     (Different from 'basic-calculator' where number=0 can also be putted to stack as it has no effect to final result.)
"""


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if not s:
            return None
        if s[0] != '[':
            return NestedInteger(int(s))
        nested, stack, l = None, [], 0   # l is the start of an number
        for i in range(len(s)):
            c = s[i]
            if c == '[':
                if nested:
                    stack.append(nested)
                nested = NestedInteger()
                l = i + 1
            elif c == ',':
                if s[i - 1] != ']':   # Attention!!!
                    number = s[l: i]
                    nested.add(int(number))
                l = i + 1
            elif c == ']':
                number = s[l: i]
                if number:  # Attention!!! corner case: '[]'
                    nested.add(NestedInteger(int(number)))
                if stack:
                    tmp = stack.pop()
                    tmp.add(nested)
                    nested = tmp
                l = i + 1
        return nested


