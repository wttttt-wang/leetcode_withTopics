"""
First Unique Character in a String
@ Hash
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        occurs = {}
        for c in s:
            occurs[c] = occurs.get(c, 0) + 1
        for i in range(len(s)):
            if occurs[s[i]] == 1:
                return i
        return -1
