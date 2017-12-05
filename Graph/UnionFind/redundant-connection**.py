"""
Redundant Connection
@ Note: Start from left to right to ensure return the right-most redundant connection.
@ Explanation: Use union find to find the link of two vertices that has already been connected, that is a loop is found.
"""


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # solution1: union-find
        parents = {}
        for n1, n2 in edges:
            parents[n1] = n1
            parents[n2] = n2
        for n1, n2 in edges:
            p1, p2 = self.find(parents, n1), self.find(parents, n2)
            if p1 == p2:
                return [n1, n2]
            parents[p1] = p2
        return []

    def find(self, parents, node):
        if parents[node] != node:
            parents[node] = self.find(parents, parents[node])
        return parents[node]
