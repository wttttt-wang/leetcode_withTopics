"""
Unique Substrings in Wraparound String
@ dp: sub-problem:
@ Attention: Removing duplicates by counting the maximum consecutive length for each character.
"""


class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:
            return 0
        dpBefore, cnts = 1, [0] * 26
        cnts[ord(p[0]) - ord('a')] = 1
        for i in range(1, len(p)):
            dpBefore = (dpBefore if self.isConsecutive(p[i - 1], p[i]) else 0) + 1
            ind = ord(p[i]) - ord('a')
            cnts[ind] = max(cnts[ind], dpBefore)
        return sum(cnts)

    def isConsecutive(self, c1, c2):
        ind1, ind2 = ord(c1) - ord('a'), ord(c2) - ord('a')
        return (ind1 + 1) % 26 == ind2
