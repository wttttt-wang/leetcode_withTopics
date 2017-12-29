"""
Min Stack
@ Stack (Monotone Stack)
"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        val = self.stack.pop()
        if self.minStack and val == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1] if self.stack else None
