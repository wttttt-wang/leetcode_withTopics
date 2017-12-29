"""
Flatten Nested List Iterator
@ Stack
@ Note: [1, [4, 6]] should return [1, 4, 6] not [1, 6, 4]!!!
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.list.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.list and not self.list[-1].isInteger():
            tmp = self.list.pop().getList()
            for i in range(len(tmp) - 1, -1, -1):   # pay attention to handle from end to start
                self.list.append(tmp[i])
        return True if self.list else False
