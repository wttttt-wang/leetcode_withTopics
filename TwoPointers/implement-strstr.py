"""
Implement strStr()
@ strStr() is a classical problem, below is a naive brute force solution using 'Two Pointers' with O(N * M) time.
  KMP maybe a better solution with O(M + N) time. But not implemented here.  QAQ
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        p1, p2 = 0, 0
        while p1 < len(haystack) and p2 < len(needle):
            if haystack[p1] == needle[p2]:
                p1 += 1
                p2 += 1
                if p2 == len(needle):
                    return p1 - len(needle)
            else:
                p1 = p1 - p2 + 1
                p2 = 0
        return -1

