"""
Word Search
@ Backtracking
"""


class Solution(object):
    visitedFlag = '-1'
    PATH_X, PATH_Y = [0, 0, -1, 1], [-1, 1, 0, 0]

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board or not board[0]:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = Solution.visitedFlag
                    if self.helper(board, word, 1, i, j):
                        return True
                    board[i][j] = word[0]
        return False

    def helper(self, board, word, startInd, startRow, startCol):
        if startInd == len(word):
            return True
        for i in range(len(Solution.PATH_X)):
            newX, newY = startRow + Solution.PATH_X[i], startCol + Solution.PATH_Y[i]
            if 0 <= newX < len(board) and 0 <= newY < len(board[0]) and board[newX][newY] == word[startInd] and \
                            board[newX][newY] != Solution.visitedFlag:
                board[newX][newY] = Solution.visitedFlag
                if self.helper(board, word, startInd + 1, newX, newY):
                    return True
                board[newX][newY] = word[startInd]
        return False

