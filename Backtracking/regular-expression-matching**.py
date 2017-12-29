"""
Regular Expression Matching
@ Backtracking + Memorization: implemented using recursion.
@ Tricky: match from end to start
@ Explanation: when there comes from a '*', there are two possibilities: (Any of it matches, the whole string matches)
                                            1. '*' stands for 0 former char
                                            2. '*' stands for 1 or more former char
               when not '*', the current s & p must match the last char.
               Match can divided into two types: 1. s[i] == p[i]  2. p[i] == '.'
"""


class Solution(object):
    cache = {}   # global cache

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if (s, p) not in self.cache:
            if not p:
                return not s
            if p[-1] == '*':
                # '*' stands for 0 former char
                if self.isMatch(s, p[:-2]):
                    self.cache[(s, p)] = True
                    return True
                # '*' stands for 1 or more former char
                if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p):
                    self.cache[(s, p)] = True
                    return True
            elif s and (p[-1] == s[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
                self.cache[(s, p)] = True
                return True
            self.cache[(s, p)] = False
        return self.cache[(s, p)]
