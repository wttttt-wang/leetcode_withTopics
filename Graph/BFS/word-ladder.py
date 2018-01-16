"""
Word Ladder
@ BFS
"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        wordList.add(beginWord)
        if endWord not in wordList:
            return 0
        neighbors = self.con_neighbors(wordList)
        # bfs
        res, queue, visited = 1, [beginWord], set([beginWord])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node == endWord:
                    return res
                for nei in neighbors[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            res += 1
        return 0

    def con_neighbors(self, wordList):
        neighbors = {}
        for word in wordList:
            neighbors[word] = []
            for c in 'qwertyuiopasdfghjklzxcvbnm':
                for i in range(len(word)):
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord != word and newWord in wordList:
                        neighbors[word].append(newWord)
        return neighbors
