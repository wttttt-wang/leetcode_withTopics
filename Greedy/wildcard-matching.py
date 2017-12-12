"""
Wildcard Matching
@ greedy: matching p[i] & s[j] when they can   (+ Two pointers)
@ O(P * S) time  & O(1) space
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        indP, indS = 0, 0
        lastStar, lastS = -1, -1
        while indS < len(s):
            if indP < len(p) and (p[indP] == '?' or p[indP] == s[indS]):
                indP += 1   # match as longest as possible
                indS += 1
            elif indP < len(p) and p[indP] == '*':
                lastStar, lastS = indP, indS   # do not increase indS to match '*' to zero char
                indP += 1
            # otherwise: not match
            elif lastStar != -1:
                indP = lastStar + 1
                lastS += 1
                indS = lastS
            else:
                return False
        while indP < len(p) and p[indP] == '*':
            indP += 1
        return indP == len(p)
