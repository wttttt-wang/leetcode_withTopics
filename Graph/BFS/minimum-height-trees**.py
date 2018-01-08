"""
Minimum Height Trees
@ BFS: The key point is that the root of MHT is the middle point(or two middle points) of the longest path in the tree.
       The solution is really tricky by using BFS to iteratively get the 'current' leaves
       until there are <= 2 leaves left which is the final result.
"""


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        indegree, neighbors = [0] * n, [[] for _ in range(n)]
        for n1, n2 in edges:
            indegree[n1] += 1
            indegree[n2] += 1
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
        leaves = []
        for i in range(n):
            if indegree[i] <= 1:
                leaves.append(i)
        left = n
        while left > 2:
            size = len(leaves)
            left -= size
            for i in range(size):
                node = leaves.pop(0)
                for nei in neighbors[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        leaves.append(nei)
        return leaves
