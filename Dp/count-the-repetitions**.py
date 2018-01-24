"""
Count The Repetitions
@ dp
"""


class Solution(object):
    _dp = {}
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if not s1 or not s2:
            return 0
        res, remaining = 0, ""
        for i in range(n1):
            remaining, cnt = self.helper(remaining + s1, s2)
            res += cnt
        return res / n2

    def helper(self, s1, s2):
        if len(s1) < len(s2):
            return s1, 0
        cnt, ind = 0, 0
        if (s1, s2) not in self._dp:
            p1, p2 = 0, 0
            while p1 < len(s1):
                if s1[p1] == s2[p2]:
                    p2 += 1
                    if p2 == len(s2):
                        cnt += 1
                        p2 = 0
                        ind = p1 + 1
                p1 += 1
            self._dp[(s1, s2)] = ("".join(s1[ind:]), cnt)
        return self._dp[(s1, s2)]


so = Solution()
print so.getMaxRepetitions("baba", 5, "baab", 1)
