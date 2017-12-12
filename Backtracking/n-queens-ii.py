"""
N-Queens II
@ No difference from N-Queens
@ Backtracking
"""


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        visitedCol = [False] * n
        visitedDiag = [False] * (2 * n - 1)
        visitedReDiag = [False] * (2 * n - 1)
        return self.helper(n, visitedCol, visitedDiag, visitedReDiag, 0, [["."] * n for i in range(n)])

    def helper(self, n, visitedCol, visitedDiag, visitedReDiag, startRow, result):
        if startRow == n:
            return 1
        res = 0
        for j in range(n):
            if visitedCol[j] or visitedDiag[startRow + j] or visitedReDiag[j - startRow + n - 1]:
                continue
            visitedCol[j] = True
            visitedDiag[startRow + j] = True
            visitedReDiag[j - startRow + n - 1] = True
            result[startRow][j] = 'Q'
            res += self.helper(n, visitedCol, visitedDiag, visitedReDiag, startRow + 1, result)
            visitedCol[j] = False
            visitedDiag[startRow + j] = False
            visitedReDiag[j - startRow + n - 1] = False
            result[startRow][j] = '.'
        return res
