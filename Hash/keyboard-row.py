"""
Keyboard Row
@ Hash
"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []
        rows = [set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']),
                set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']), set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])]
        results = []
        for w in words:
            if self.isValid(w, rows):
                results.append(w)
        return results

    def isValid(self, word, rows):
        if not word:
            return True
        flagRow = None
        for r in rows:
            if word[0].lower() in r:
                flagRow = r
                break
        for c in word:
            if c.lower() not in flagRow:
                return False
        return True
