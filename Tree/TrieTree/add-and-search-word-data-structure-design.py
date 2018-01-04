"""
Add and Search Word - Data structure design
@ Trie Tree
"""


class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.children = [None] * 26


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if not word:
            return
        ind, root = 0, self.trie
        while ind < len(word):
            charInd = ord(word[ind]) - ord('a')
            if not root.children[charInd]:
                root.children[charInd] = TrieNode()
            root = root.children[charInd]
            ind += 1
        root.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(word, 0, self.trie)

    def searchHelper(self, word, ind, root):
        if ind >= len(word):
            return root and root.isWord
        if word[ind] == '.':
            for child in root.children:
                if child:
                    if self.searchHelper(word, ind + 1, child):
                        return True
        else:
            charInd = ord(word[ind]) - ord('a')
            if root.children[charInd]:
                return self.searchHelper(word, ind + 1, root.children[charInd])
        return False
