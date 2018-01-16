"""
Range Sum Query 2D - Immutable
@ dp + Math
@ Note: Should pay attention to the index!!! When operate on rectangles, pay attention to the margins!!!
"""


class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if not matrix or not matrix[0]:
            self.subRegin = [[]]
            return
        rowNum, colNum = len(matrix), len(matrix[0])
        self.subRegion = [[0 for _ in range(colNum + 1)]]
        for row in range(rowNum):
            self.subRegion.append([])
            self.subRegion[row + 1].append(0)
            for col in range(colNum):
                val = self.subRegion[row + 1][col] + self.subRegion[row][col + 1] - self.subRegion[row][col] + \
                      matrix[row][col]
                self.subRegion[row + 1].append(val)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 > row2 or col1 > col2:
            return 0
        row1 = row1 if row1 >= 0 else 0
        row2 = row2 if row2 < len(self.matrix) else len(self.matrix) - 1
        col1 = col1 if col1 >= 0 else 0
        col2 = col2 if col2 < len(self.matrix[0]) else len(self.marix[0]) - 1
        return self.subRegion[row2 + 1][col2 + 1] - self.subRegion[row2 + 1][col1] - self.subRegion[row1][col2 + 1] \
               + self.subRegion[row1][col1]   # Attention to the index!!!
