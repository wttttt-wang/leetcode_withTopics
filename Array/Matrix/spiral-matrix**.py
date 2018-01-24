"""
spiral-matrix
@ Array(Matrix): ummm... The solution below is very neat.
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        startRow, endRow = 0, len(matrix) - 1
        startCol, endCol = 0, len(matrix[0]) - 1
        results = []
        while startRow <= endRow and startCol <= endCol:
            # 1. traverse right
            for j in range(startCol, endCol + 1):
                results.append(matrix[startRow][j])
            startRow += 1
            # 2. traverse down
            for i in range(startRow, endRow + 1):
                results.append(matrix[i][endCol])
            endCol -= 1
            # 3. traverse left
            if startRow <= endRow:
                for j in range(endCol, startCol - 1, -1):
                    results.append(matrix[endRow][j])
            endRow -= 1
            # 4. traverse up
            if startCol <= endCol:
                for i in range(endRow, startRow - 1, -1):
                    results.append(matrix[i][startCol])
            startCol += 1
        return results
