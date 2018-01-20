"""
Implement Stack using Queues
@ Design + Stack + Queue: Using one or two queue are all acceptable. The key point is put the element in the right pos.
"""


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        # move
        for i in range(len(self.stack) - 1, 0, -1):
            self.stack[i] = self.stack[i - 1]
        self.stack[0] = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack) == 0
