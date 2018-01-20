"""
Implement Queue using Stacks
@ Design + Stack + Queue
"""


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        for i in range(len(self.queue) - 1, 0, -1):
            self.queue[i] = self.queue[i - 1]
        self.queue[0] = x

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.queue.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) == 0
