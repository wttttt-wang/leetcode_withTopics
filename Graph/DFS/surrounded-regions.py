"""
Surrounded Regions
@ DFS/BFS
@ More: 1. this problem can also use union-find, but I think DFS is easier for solving it.
        2. DFS from surrounding nodes can leave out use of 'visited' > <
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        # 1. from all surrounders flag 'O' that cannot be captured as FLAG
        FLAG = -1
        PATH_X, PATH_Y = [-1, 1, 0, 0], [0, 0, -1, 1]
        queue = []
        m, n = len(board), len(board[0])
        for j in range(n):
            if board[0][j] == 'O':
                queue.append((0, j))
                board[0][j] = FLAG
            if board[-1][j] == 'O':
                queue.append((m - 1, j))
                board[-1][j] = FLAG
        for i in range(1, m - 1):
            if board[i][0] == 'O':
                queue.append((i, 0))
                board[i][0] = FLAG
            if board[i][-1] == "O":
                queue.append((i, n - 1))
                board[i][-1] = FLAG
        while queue:
            x, y = queue.pop()  # DFS
            for i in range(len(PATH_X)):
                newX, newY = x + PATH_X[i], y + PATH_Y[i]
                if 0 <= newX < m and 0 <= newY < n and board[newX][newY] == 'O':
                    queue.append((newX, newY))
                    board[newX][newY] = FLAG
        # mark flag as 'O' else as 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == FLAG:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
