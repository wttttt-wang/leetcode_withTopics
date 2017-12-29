"""
Basic Calculator
@ Stack
@ Note: For more concise solution see SolutionV2.
@ Note: See 'Stack/mini-parser.py' for similar problem.
"""


class SolutionV2(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, number, sign, res = [], 0, 1, 0
        for i in range(len(s)):
            if s[i].isdigit():
                number = number * 10 + int(s[i])
            elif s[i] == '+':
                res += sign * number
                number = 0
                sign = 1
            elif s[i] == '-':
                res += sign * number
                number = 0
                sign = -1
            elif s[i] == '(':
                stack.append(res)    # only append to stack for '('
                stack.append(sign)   # first res and then sign (because sign is for the next number)
                res, sign = 0, 1
            elif s[i] == ')':
                res += sign * number
                number = 0
                res *= stack.pop()
                res += stack.pop()
        if number:
            res += sign * number
        return res


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = '(' + s + ')'
        res, ind, stack = 0, 0, []
        while ind < len(s):
            if s[ind] == ' ':
                pass
            elif s[ind] == ')':
                tmp = 0
                while stack and stack[-1] != '(':
                    t1 = int(stack.pop())
                    if stack and stack[-1] != '(' and stack.pop() == '-':
                        tmp -= t1
                    else:
                        tmp += t1
                if stack:
                    stack.pop()
                stack.append(tmp)
            elif s[ind].isdigit():
                tmp = int(s[ind])
                while ind < len(s) - 1 and s[ind + 1].isdigit():
                    ind += 1
                    tmp = tmp * 10 + int(s[ind])
                stack.append(tmp)
            else:
                stack.append(s[ind])
            ind += 1
        return stack[-1]

so = SolutionV2()
print so.calculate("(1+(4+5)-3)+6")
