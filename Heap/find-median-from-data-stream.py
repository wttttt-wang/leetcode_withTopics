"""
Find Median from Data Stream
@ Heap
@ Note: Just using two heaps without a median can make the solution more concise.
"""

from heapq import *


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller, self.bigger = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.smaller) < len(self.bigger):
            heappush(self.bigger, num)
            heappush(self.smaller, -heappop(self.bigger))
        else:
            heappush(self.smaller, -num)
            heappush(self.bigger, -heappop(self.smaller))

    def findMedian(self):
        """
        :rtype: float
        """
        return self.bigger[0] if len(self.bigger) > len(self.smaller) else (self.bigger[0] - self.smaller[0]) / 2.0
