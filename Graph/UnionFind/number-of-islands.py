"""
Number of Islands
@ Note: To use union-find, should flatten (x, y) first --> v = n * x + y where n is column num of matrix
        Actually I recommend using DFS/BFS to solve this problem.
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        PATH_X, PATH_Y = [-1, 0], [0, -1]
        unf = UnionFind(grid)
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '0':
                    continue
                for i in range(len(PATH_X)):
                    newX, newY = x + PATH_X[i], y + PATH_Y[i]
                    if 0 <= newX < m and 0 <= newY < n and grid[newX][newY] == '1':
                        unf.connect(x * n + y, newX * n + newY)
        return unf.cnt


class UnionFind(object):
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.parents = [i for i in range(m * n)]
        self.cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.cnt += 1

    def connect(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.cnt -= 1   # cnt - 1 when connect two 'origin' disconnect part
            self.parents[px] = py

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
