"""
Longest Substring Without Repeating Characters
@ Two Pointers + Hash
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        occurs = {}
        res = 0
        for r in range(len(s)):
            if s[r] in occurs:
                left = max(left, occurs[s[r]] + 1)
            occurs[s[r]] = r
            res = max(res, r - left + 1)
        return res

