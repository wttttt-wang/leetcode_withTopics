"""
Maximum Product of Word Lengths
@ Bit Manipulation + Hash
@ Note to store the maximum length of each unique bit presentation.
"""


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        res = 0
        word2bit = {}  # bit: maxLen word
        for w in words:
            bit = self.getBit(w)
            word2bit[bit] = max(word2bit.get(bit, 0), len(w))
        bits = word2bit.keys()
        for i in range(len(bits)):
            for j in range(i + 1, len(bits)):
                if not bits[i] & bits[j]:
                    res = max(res, word2bit[bits[i]] * word2bit[bits[j]])
        return res

    def getBit(self, word):
        res = 0
        for w in set(word):
            res += (1 << (ord(w) - ord('a')))
        return res

