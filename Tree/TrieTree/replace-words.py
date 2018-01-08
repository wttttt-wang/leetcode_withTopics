"""
Replace Words
@ Trie Tree: Nothing special.
"""


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if not dict:
            return sentence
        tree = TrieTree()
        for w in dict:
            tree.add(w)
        words, results = sentence.split(), []
        for w in words:
            results.append(tree.findPre(w))
        return " ".join(results)


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

    def findPre(self, w):
        root = self.root
        for i in range(len(w)):
            if root.isWord:
                return w[:i]
            ind = ord(w[i]) - ord('a')
            if not root.children[ind]:
                return w
            root = root.children[ind]
        return w
