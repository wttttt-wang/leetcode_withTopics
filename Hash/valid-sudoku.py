"""
Valid Sudoku
@ Hash
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m = 9
        if not board or not board[0] or len(board) != m or len(board[0]) != m:
            return False
        visitedRow, visitedCol, visitedCell = [[False] * m for _ in range(m)], [[False] * m for _ in range(m)], [
            [False] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                if board[i][j] == '.':
                    continue
                val = int(board[i][j])
                if not 0 < val < 10:
                    return False
                if visitedRow[i][val - 1] or visitedCol[j][val - 1] or visitedCell[(i / 3) * 3 + (j / 3)][val - 1]:
                    return False
                visitedRow[i][val - 1], visitedCol[j][val - 1], visitedCell[(i / 3) * 3 + (j / 3)][
                    val - 1] = True, True, True
        return True

