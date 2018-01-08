"""
Course Schedule
@ Graph + Topological Sort + DFS/BFS
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses <= 0 or not prerequisites:
            return True
        neighbors = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for p1, p2 in prerequisites:
            neighbors[p1].append(p2)
            indegree[p2] += 1
        heap, cnt = [], 0
        for i in range(len(neighbors)):
            if not indegree[i]:
                heap.append(i)
                cnt += 1
        while heap:
            node = heap.pop()
            for nei in neighbors[node]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    heap.append(nei)
                    cnt += 1
        return cnt == numCourses

