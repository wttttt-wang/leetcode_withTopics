"""
Valid Anagram
@ Hash
"""


class SolutionV2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        occurs_s = [0] * 26
        for c in s:
            occurs_s[ord(c) - ord('a')] += 1
        for c in t:
            occurs_s[ord(c) - ord('a')] -= 1
            if occurs_s[ord(c) - ord('a')] < 0:
                return False
        return True


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        occurs = {}
        for val in s:
            occurs[val] = occurs.get(val, 0) + 1
        for val in t:
            if not occurs.get(val, 0):
                return False
            occurs[val] -= 1
        return True if not sum(occurs.values()) else False  # do not forget to check this!!!
