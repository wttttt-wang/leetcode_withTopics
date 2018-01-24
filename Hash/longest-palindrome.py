"""
Longest Palindrome
@ Hash
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        occurs = {}
        for c in s:
            occurs[c] = occurs.get(c, 0) + 1
        res, single = 0, False
        for key in occurs:
            if occurs[key] % 2:
                if not single:
                    res += 1
                    single = True
                res += (occurs[key] - 1)
            else:
                res += occurs[key]
        return res
