"""
Word Pattern
@ Hash
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split()  # Also one-to-one mapping
        if len(pattern) != len(strs):
            return False
        p2s, used_s = [None] * 26, set()
        for i in range(len(strs)):
            c = ord(pattern[i]) - ord('a')
            if not p2s[c]:
                if strs[i] in used_s:
                    return False
                p2s[c] = strs[i]
                used_s.add(strs[i])
            elif p2s[c] != strs[i]:
                return False
        return True

