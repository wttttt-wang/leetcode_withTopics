"""
N-Queens
@ Backtracking
@ Tricky: how to represent diagonal & reverse-diagonal
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        visitedCol = [False] * n
        visitedDiag = [False] * (2 * n - 1)
        visitedReDiag = [False] * (2 * n - 1)
        results = []
        self.helper(n, visitedCol, visitedDiag, visitedReDiag, 0, [["."] * n for i in range(n)], results)
        return results

    def helper(self, n, visitedCol, visitedDiag, visitedReDiag, startRow, result, results):
        if startRow == n:
            results.append(["".join(line) for line in result])
            return
        for j in range(n):
            if visitedCol[j] or visitedDiag[startRow + j] or visitedReDiag[j - startRow + n - 1]:
                continue
            visitedCol[j] = True
            visitedDiag[startRow + j] = True
            visitedReDiag[j - startRow + n - 1] = True
            result[startRow][j] = 'Q'
            self.helper(n, visitedCol, visitedDiag, visitedReDiag, startRow + 1, result, results)
            visitedCol[j] = False
            visitedDiag[startRow + j] = False
            visitedReDiag[j - startRow + n - 1] = False
            result[startRow][j] = '.'
