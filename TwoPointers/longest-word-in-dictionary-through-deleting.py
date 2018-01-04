"""
Longest Word in Dictionary through Deleting
@ Two pointers + Sort
"""


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        if not d:
            return ""
        d.sort(cmp=lambda x, y: -1 if len(x) > len(y) or (len(x) == len(y) and x < y) else 1)
        for c in d:
            p1, p2 = 0, 0
            while p1 < len(s) and p2 < len(c):
                if s[p1] == c[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    p1 += 1
            if p2 >= len(c):
                return c
        return ""


