"""
Island Perimeter
@ Math: res = (number of islands) * 4 - (number of neighboring edges) * 2
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islandCnt, neighCnt = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    islandCnt += 1
                    if i > 0 and grid[i - 1][j]:
                        neighCnt += 1
                    if j > 0 and grid[i][j - 1]:
                        neighCnt += 1
        return islandCnt * 4 - neighCnt * 2
