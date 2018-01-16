"""
Scramble String
@ Recursion + Memorization: Memorization for speeding up. The key point is how to split for recursion.
"""


class Solution(object):
    _dp = {('', ''): True}

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        dp = self._dp
        if (s1, s2) in dp:
            return dp[(s1, s2)]
        if not s1:
            return not s2
        if not s2 or len(s1) != len(s2) or sorted(s1) != sorted(s2):   # For speeding up
            return False
        if s1 == s2:
            return True
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                dp[(s1, s2)] = True
                return True
            if self.isScramble(s1[:i], s2[len(s2) - i: len(s2)]) and self.isScramble(s1[i:], s2[:len(s2) - i]):
                dp[(s1, s2)] = True
                return True
        dp[(s1, s2)] = False
        return False
