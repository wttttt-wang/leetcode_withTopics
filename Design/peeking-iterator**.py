"""
Peeking Iterator
@ Design: The key point is to cache the next element.
"""


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.tmpNext = iterator.next() if iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.tmpNext

    def next(self):
        """
        :rtype: int
        """
        res = self.tmpNext
        self.tmpNext = self.iter.next() if self.iter.hasNext() else None
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.tmpNext is not None
