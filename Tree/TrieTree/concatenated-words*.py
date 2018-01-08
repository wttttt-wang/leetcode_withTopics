"""
Concatenated Words
@ Trie Tree
@ Note: Have no idea why this will TLE.
"""


class TrieNode(object):
    def __init__(self):
        self.children, self.isWord = [None] * 26, False


class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, w):
        root = self.root
        for val in w:
            ind = ord(val) - ord('a')
            if not root.children[ind]:
                root.children[ind] = TrieNode()
            root = root.children[ind]
        root.isWord = True

    def check(self, w):
        if not w:
            return self.root.isWord
        root = self.root
        for i in range(len(w)):
            ind = ord(w[i]) - ord('a')
            if not root.children[ind]:
                return False
            root = root.children[ind]
            if root.isWord and self.check(w[i + 1:]):
                return True
        return root and root.isWord


class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        results = []
        tree = TrieTree()
        words.sort(key=lambda x: len(x))
        for w in words:
            if not w:
                continue
            if tree.check(w):
                results.append(w)
            tree.add(w)
        return results


so = Solution()
print so.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])
