"""
 Implement Magic Dictionary
 @ Trie Tree
"""


class TrieNode(object):
    def __init__(self):
        self.children, self.isWord = [None] * 26, False


class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.root = TrieNode()
        for w in dict:
            self.insert(w)

    def insert(self, w):
        root = self.root
        for val in w:
            ind = ord(val) - ord('a')
            if not root.children[ind]:
                root.children[ind] = TrieNode()
            root = root.children[ind]
        root.isWord = True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        root = self.root
        for i in range(len(word)):
            if not root:
                return False
            ind = ord(word[i]) - ord('a')
            for j in range(26):
                if j != ind and self.searchHelper(word[i + 1:], root.children[j]):
                    return True
            root = root.children[ind]
        return False

    def searchHelper(self, word, root):
        for val in word:
            if not root:
                return False
            ind = ord(val) - ord('a')
            root = root.children[ind]
        return root and root.isWord
