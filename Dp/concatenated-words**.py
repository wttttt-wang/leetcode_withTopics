"""
Concatenated Words
@ dp: The key point is to sort first to reduce unnecessary search.
@ Note: A concatenated word is defined as a string that is comprised entirely of **shorter** words in the given array.
"""


class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        results = []
        # Attention: Sort first. For a string is comprised of **shorter** words. Can skip unnecessary search!
        words.sort(key=lambda x: len(x))
        concate = set()
        for w in words:
            if self.canForm(w, concate):
                results.append(w)
            concate.add(w)
        return results

    def canForm(self, word, concate):
        if not concate:
            return False
        dp = [False] * (len(word) + 1)
        dp[0] = True
        for i in range(1, len(word) + 1):
            for j in range(i):
                if dp[j] and word[j:i] in concate:
                    dp[i] = True
                    break
        return dp[-1]
