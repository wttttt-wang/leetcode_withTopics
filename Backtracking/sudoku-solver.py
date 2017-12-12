"""
Sudoku Solver
@ Classical Backtracking problem
"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        # backtracking
        visitedRow = [[False] * 9 for _ in range(9)]
        visitedCol = [[False] * 9 for _ in range(9)]
        visitedMat = [[False] * 9 for _ in range(9)]
        # 1. initialize visited
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                val = int(board[i][j]) - 1
                visitedRow[i][val] = True
                visitedCol[j][val] = True
                visitedMat[(i / 3) * 3 + j / 3][val] = True
        self.helper(board, visitedRow, visitedCol, visitedMat)

    def helper(self, board, visitedRow, visitedCol, visitedMat):
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                for val in range(9):
                    if visitedRow[i][val] or visitedCol[j][val] or visitedMat[(i / 3) * 3 + j / 3][val]:
                        continue
                    board[i][j] = str(val + 1)
                    visitedRow[i][val] = True
                    visitedCol[j][val] = True
                    visitedMat[(i / 3) * 3 + j / 3][val] = True
                    if self.helper(board, visitedRow, visitedCol, visitedMat):
                        return True
                    board[i][j] = '.'
                    visitedRow[i][val] = False
                    visitedCol[j][val] = False
                    visitedMat[(i / 3) * 3 + j / 3][val] = False
                return False   # Attention: This is important!!!
        return True

so = Solution()
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
print so.solveSudoku(board)
print board
