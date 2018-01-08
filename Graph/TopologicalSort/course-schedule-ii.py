"""
Course Schedule II
@ Graph + Topological Sort + DFS/BFS
"""


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses <= 0:
            return []
        indegree, neighbors = [0] * numCourses, [[] for _ in range(numCourses)]
        for p1, p2 in prerequisites:
            indegree[p1] += 1
            neighbors[p2].append(p1)
        heap, results = [], []
        for i in range(len(indegree)):
            if not indegree[i]:
                heap.append(i)
        while heap:
            node = heap.pop()
            results.append(node)
            for nei in neighbors[node]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    heap.append(nei)
        return results if len(results) == numCourses else []
