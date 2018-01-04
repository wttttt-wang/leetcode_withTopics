"""
Word Search II
@ Trie Tree: The method is not that complicated, but the realization is really fussy = =
"""


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not words or not board or not board[0]:
            return []
        # 1. construct trie tree for words
        trie = TrieTree()
        for w in words:
            trie.add(w)
        # 2. search
        m, n = len(board), len(board[0])
        results = set()
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                trie.search(board, i, j, visited, results, [board[i][j]])
                visited[i][j] = False
        return list(results)


class TrieNode(object):
    def __init__(self):
        self.children, self.isWord = [None] * 26, False


class TrieTree(object):
    def __init__(self):
        self.trie = TrieNode()

    def add(self, word):
        if not word:
            self.trie.isWord = True
            return
        ind, root = 0, self.trie
        while ind < len(word):
            charInd = ord(word[ind]) - ord('a')
            if not root.children[charInd]:
                root.children[charInd] = TrieNode()
            root = root.children[charInd]
            ind += 1
        root.isWord = True

    def search(self, board, row, col, visited, results, result):
        self.searchHelper(board, row, col, visited, results, self.trie.children[ord(board[row][col]) - ord('a')],
                          result)

    def searchHelper(self, board, row, col, visited, results, root, result):
        if not root:
            return
        if root.isWord:
            results.add("".join(result))
        m, n = len(board), len(board[0])
        PATH_X, PATH_Y = [1, -1, 0, 0], [0, 0, -1, 1]
        for x in range(len(PATH_X)):
            newRow, newCol = row + PATH_X[x], col + PATH_Y[x]
            if 0 <= newRow < m and 0 <= newCol < n and not visited[newRow][newCol]:
                result.append(board[newRow][newCol])
                visited[newRow][newCol] = True
                self.searchHelper(board, newRow, newCol, visited, results,
                                  root.children[ord(board[newRow][newCol]) - ord('a')], result)
                visited[newRow][newCol] = False
                result.pop()

