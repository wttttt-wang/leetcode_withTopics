"""
Implement Trie (Prefix Tree)
@ Trie Tree
@ Note: All implementation can be done with non-recursion. --> This is recommended.
"""


class TrieNode(object):
    def __init__(self):
        self.children, self.isWord = [None] * 26, False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self.root
        for w in word:
            ind = ord(w) - ord('a')
            if not root.children[ind]:
                root.children[ind] = TrieNode()
            root = root.children[ind]
        root.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for char in word:
            ind = ord(char) - ord('a')
            if not root or not root.children[ind]:
                return False
            root = root.children[ind]
        return root.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for c in prefix:
            ind = ord(c) - ord('a')
            if not root or not root.children[ind]:
                return False
            root = root.children[ind]
        return True

