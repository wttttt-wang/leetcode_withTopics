"""
Word Ladder II
@ BFS + DFS:  1. BFS to find the smallDis from endWord to all other words. (For guiding us to dfs the right direction).
              2. DFS to get all smallest routine.
@ Corner case:  1. cannot reach from endWord to beginWord
                2. endWord not in wordList
"""


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        allWords = set(wordList)
        allWords.add(beginWord)  # Attention: Cannot add endWord
        if endWord not in allWords:
            return[]
        # 1. construct graph
        neighbors = self.construct_graph(allWords)
        # 2. bfs to get the smallest distance from endWord to allWords
        smallDis = self.bfs_small_dis(neighbors, endWord, beginWord)
        # 3. dfs to get all smallest routine
        results = []
        if beginWord not in smallDis:
            return []   # Attention: return [] if cannot reach from endWord to beginWord
        self.dfs_results(neighbors, beginWord, endWord, smallDis, [beginWord], results, smallDis[beginWord])
        return results

    def dfs_results(self, neighbors, beginWord, endWord, smallDis, result, results, currDis):
        if beginWord == endWord:
            results.append(result[:])
            return
        for nei in neighbors[beginWord]:
            if smallDis[nei] == currDis - 1:
                result.append(nei)
                self.dfs_results(neighbors, nei, endWord, smallDis, result, results, currDis - 1)
                result.pop()

    def construct_graph(self, words):
        neighbors = {}
        for w in words:
            neighbors[w] = []
            for i in range(len(w)):
                for c in 'qwertyuiopasdfghjklzxcvbnm':
                    newWord = w[:i] + c + w[i + 1:]
                    if newWord != w and newWord in words:
                        neighbors[w].append(newWord)
        return neighbors

    def bfs_small_dis(self, neighbors, endWord, beginWord):
        queue = [endWord]
        smallDis = {}
        dis = 0
        visited = set([endWord])
        while queue:
            size = len(queue)
            for i in range(size):
                word = queue.pop(0)
                smallDis[word] = dis
                if word == beginWord:
                    break
                for nei in neighbors[word]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            dis += 1
        return smallDis


so = Solution()
print so.findLadders("hot", "dog", ["hot", "dog"])
