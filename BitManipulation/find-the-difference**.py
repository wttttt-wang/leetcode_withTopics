"""
Find the Difference
@ Bit Manipulation: The solution is really tricky > <
                    But it's also same as 'single-number' after unwrapping it.
"""


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a, b = self.getxor(s), self.getxor(t)
        return chr(a ^ b)

    def getxor(self, s):
        res = 0
        for v in s:
            res ^= ord(v)
        return res
