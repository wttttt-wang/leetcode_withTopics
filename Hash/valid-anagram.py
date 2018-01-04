"""
Valid Anagram
@ Hash
"""


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

