"""
Search a 2D Matrix
@ Binary search: first on matrix[:][0] then on matrix[row][:]
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        # 1. binary search on col: right-most <=
        left, right = 0, m - 1
        while left < right - 1:
            mid = (right - left) / 2 + left
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                left = mid
            else:
                right = mid
        if matrix[right][0] <= target:
            row = right
        elif matrix[left][0] <= target:
            row = left
        else:
            return False
        # 2. binary search on row
        left, right = 0, n - 1
        while left < right - 1:
            mid = (right - left) / 2 + left
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                left = mid
            else:
                right = mid
        return matrix[row][left] == target or matrix[row][right] == target

