"""
Friend Circles: Equivalent to finding connected components in a graph.
                So both DFS/Union-Find will work.
@ Note: The point is to when u connect to 'origin' disconnected part, subtract res as connected components decreased.
"""


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        m, n = len(M), len(M[0])
        res = m
        parents = [i for i in range(m)]
        for x in range(m):
            for y in range(x + 1, n):
                if M[x][y] == 1:
                    p1, p2 = self.find(x, parents), self.find(y, parents)
                    if p1 != p2:
                        res -= 1
                        parents[p1] = p2
        return res

    def find(self, x, parents):
        if parents[x] != x:
            parents[x] = self.find(parents[x], parents)
        return parents[x]
