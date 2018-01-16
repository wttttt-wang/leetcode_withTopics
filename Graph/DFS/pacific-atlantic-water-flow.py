"""
Pacific Atlantic Water Flow
@ DFS: The solution itself is not difficult. But have spent some time understand the problem. = =
"""


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        pac, visited_pac = [], set()
        atl, visited_atl = [], set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            pac.append((i, 0))
            visited_pac.add((i, 0))
            atl.append((i, n - 1))
            visited_atl.add((i, n - 1))
        for j in range(n):
            pac.append((0, j))
            visited_pac.add((0, j))
            atl.append((m - 1, j))
            visited_atl.add((m - 1, j))
        self.bfsHelper(pac, visited_pac, matrix)
        self.bfsHelper(atl, visited_atl, matrix)
        return list(visited_pac & visited_atl)

    def bfsHelper(self, queue, visited, matrix):
        PATH_X, PATH_Y = [0, 0, -1, 1], [-1, 1, 0, 0]
        m, n = len(matrix), len(matrix[0])
        while queue:
            x, y = queue.pop()
            for i in range(len(PATH_X)):
                newX, newY = x + PATH_X[i], y + PATH_Y[i]
                if 0 <= newX < m and 0 <= newY < n and matrix[newX][newY] >= matrix[x][y] and (
                newX, newY) not in visited:
                    queue.append((newX, newY))
                    visited.add((newX, newY))
