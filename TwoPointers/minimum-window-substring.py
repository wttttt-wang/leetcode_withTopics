"""
Minimum Window Substring
@ Two pointers  + Hash
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        target = {}
        for c in t:
            target[c] = target.get(c, 0) + 1
        p1, p2 = 0, 0
        occurs = {}
        occurNum = 0
        res, minLen = None, None
        while p2 < len(s):
            if target.get(s[p2], 0) > occurs.get(s[p2], 0):
                occurNum += 1    # update occurNum only when hit
            occurs[s[p2]] = occurs.get(s[p2], 0) + 1
            if occurNum == len(t):
                # update p1 to get current minimum window
                while p1 <= p2 and occurs.get(s[p1], 0) > target.get(s[p1], 0):
                    occurs[s[p1]] -= 1
                    p1 += 1
                if minLen is None or p2 - p1 + 1 < minLen:
                    minLen = p2 - p1 + 1
                    res = (p1, p2)
                occurs[s[p1]] -= 1
                p1 += 1
                occurNum -= 1
            p2 += 1
        return "" if not res else s[res[0]: res[1] + 1]


so = Solution()
print so.minWindow("ADOBECODEBANC", "ABC")
