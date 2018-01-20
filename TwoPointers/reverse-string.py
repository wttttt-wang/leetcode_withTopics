"""
Reverse String
@ Two pointers + String
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        left, right = 0, len(s) - 1
        res = list(s)
        while left < right:
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1
        return "".join(res)

