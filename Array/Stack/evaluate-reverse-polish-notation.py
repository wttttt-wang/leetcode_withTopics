"""
Evaluate Reverse Polish Notation
@ Stack
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        stack = []
        for t in tokens:
            if t in '+-/*':
                self.calcu(stack, t)
            else:
                stack.append(int(t))
        return stack[-1]

    def calcu(self, stack, t):
        if not stack or len(stack) < 2:
            stack = []
            return
        t2, t1 = stack.pop(), stack.pop()
        if t == '+':
            stack.append(t1 + t2)
        elif t == '-':
            stack.append(t1 - t2)
        elif t == '*':
            stack.append(t1 * t2)
        else:
            stack.append(int(float(t1) / t2))
        return

