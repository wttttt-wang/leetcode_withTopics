"""
Search a 2D Matrix II
@ Divide And Conquer: To start from the left corner, this is really a tricky for removing useless searching.
@ O(M + N) time
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
        row, col = m - 1, 0
        # Divide And Conquer: O(M + N) time
        while row >= 0 and col < n:
            if target == matrix[row][col]:
                return True
            if matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        return False
