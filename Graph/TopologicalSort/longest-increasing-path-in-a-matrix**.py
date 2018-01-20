"""
Longest Increasing Path in a Matrix
@ Topological Sort + BFS: The key point is maxLen[i][j] is determined by all smaller values around matrix[i][j].
                          When maxLen of smaller surrounding values determined, maxLen[i][j] can be determined.
                          This is why topological sort works. (The solution is really interesting > <)
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        indegree = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j < n - 1:
                    if matrix[i][j] > matrix[i][j + 1]:
                        indegree[i][j] += 1
                    elif matrix[i][j] < matrix[i][j + 1]:
                        indegree[i][j + 1] += 1
                if i < m - 1:
                    if matrix[i][j] > matrix[i + 1][j]:
                        indegree[i][j] += 1
                    elif matrix[i][j] < matrix[i + 1][j]:
                        indegree[i + 1][j] += 1
        res, heap = 0, []
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    heap.append((i, j))
        PATH_X, PATH_Y = [0, 0, 1, -1], [1, -1, 0, 0]
        while heap:
            res += 1
            size = len(heap)
            for i in range(size):
                x, y = heap.pop(0)
                for e in range(len(PATH_X)):
                    newX, newY = x + PATH_X[e], y + PATH_Y[e]
                    if 0 <= newX < m and 0 <= newY < n and matrix[newX][newY] > matrix[x][y]:
                        indegree[newX][newY] -= 1
                        if not indegree[newX][newY]:
                            heap.append((newX, newY))
        return res

