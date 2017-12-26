"""
Queue Reconstruction by Height
@ Greedy
@ The key point is how to sort the array
@ O(N ^ 2) for inserting each time
@ Note: pay attention to the way to sort by two elements
"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        people.sort(key=lambda (h, k): (-h, k))  # first sort by h asc, k desc if h equals
        res = []
        for val in people:
            res.insert(val[1], val)
        return res
