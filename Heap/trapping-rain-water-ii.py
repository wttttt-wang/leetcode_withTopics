"""
Trapping Rain Water II
@ Heap: The key point is the minimum wrapper height determines the capacity.
@ Note that should use wrapper higher height to update inner column's height.
"""


from heapq import *


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0] or len(heightMap) <= 2 or len(heightMap[0]) <= 2:
            return 0
        res, heap, visitedFlag = 0, [], -1
        PATH_X, PATH_Y = [-1, 1, 0, 0], [0, 0, -1, 1]
        m, n = len(heightMap), len(heightMap[0])
        # 1. initialize heap
        for j in range(n):
            heappush(heap, (heightMap[0][j], 0, j))
            heappush(heap, (heightMap[m - 1][j], m - 1, j))
            heightMap[0][j], heightMap[m - 1][j] = visitedFlag, visitedFlag
        for i in range(1, m - 1):
            heappush(heap, (heightMap[i][0], i, 0))
            heappush(heap, (heightMap[i][n - 1], i, n - 1))
            heightMap[i][0], heightMap[i][n - 1] = visitedFlag, visitedFlag
        while heap:
            height, x, y = heappop(heap)
            for p in range(len(PATH_X)):
                newX, newY = x + PATH_X[p], y + PATH_Y[p]
                if 0 <= newX < m and 0 <= newY < n and heightMap[newX][newY] != visitedFlag:
                    heappush(heap, (max(heightMap[newX][newY], height), newX, newY))
                    res += max(0, height - heightMap[newX][newY])
                    heightMap[newX][newY] = visitedFlag
        return res
