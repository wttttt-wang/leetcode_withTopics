"""
Isomorphic Strings
@ Hash: Note that should be one to one mapping.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s2t, usedt = {}, set()
        for i in range(len(s)):
            if s[i] in s2t:
                if t[i] != s2t[s[i]]:
                    return False
            else:
                if t[i] in usedt:
                    return False
                usedt.add(t[i])
                s2t[s[i]] = t[i]
        return True
