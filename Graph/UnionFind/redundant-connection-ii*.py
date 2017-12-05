"""
Redundant Connection II
@ Note: Start from left to right to ensure return the right-most redundant connection.
@ Explanation: There are two cases make the tree invalid:
               1. one node with in-degree = 2
               2. the directed graph contains loop
    And there exists three situations:
    1. just one node whose in-degree = 2 & no loop
    2. loop & not exists node whose in-degree = 2
    3. loop & exists node whose in-degree = 2
@ Implementation: 1. find the two links that makes it's vertex's in-degree = 2, they are candidates.
                  2. mark the second candidate(link) as invalid  (if exists)
                  3. use union-find(as 'Redundant Connection') to check if there is loop
                  4. if loop found: return the last link if candidates empty else the first candidate
                  5. else: return the second candidate
@ Note: after mark the second candidate, there is no node whose in-degree = 2. Then union-find can work well
        for finding loop.
        As union-find does not work well for situation like [[1,2], [1,3], [2,3]].
"""


class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges) + 1
        parents = [i for i in range(n)]
        hasParent = [None] * n
        candidate = [None, None]
        # 1. initialize union-find's parents & find the candidate links that makes it's vertex indegree=2
        for link in edges:
            n1, n2 = link
            parents[n1] = n1
            parents[n2] = n2
            if hasParent[n2]:
                candidate[0] = hasParent[n2]
                candidate[1] = [n1, n2]
                link[1] = -1  # mark this link as invalid
            hasParent[n2] = [n1, n2]
        # union find
        for n1, n2 in edges:
            if n2 == -1:
                continue
            p1, p2 = self.find(n1, parents), self.find(n2, parents)
            if p1 == p2:
                if not candidate[0]:
                    return [n1, n2]  # not exists vertex whose indegree=2
                return candidate[0]
            parents[p1] = p2
        return candidate[1]

    def find(self, node, parents):
        if parents[node] != node:
            parents[node] = self.find(parents[node], parents)
        return parents[node]

