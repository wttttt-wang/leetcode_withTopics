"""
Assign Cookies
@ Greedy + Two pointers: The key point is always give the cookies to the child with smaller greed factor.
"""


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s:
            return 0
        g.sort()
        s.sort()
        pg, ps, res = 0, 0, 0
        while pg < len(g) and ps < len(s):
            while ps < len(s) and s[ps] < g[pg]:
                ps += 1
            if ps < len(s):
                res += 1
                ps += 1
                pg += 1
        return res

