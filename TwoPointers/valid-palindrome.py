"""
Valid Palindrome
@ Two pointers: Nothing special
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not (s[left].isalpha() or s[left].isdigit()):
                left += 1
            while left < right and not (s[right].isalpha() or s[right].isdigit()):
                right -= 1
            a, b = s[left].lower(), s[right].lower()
            if a != b:
                return False
            left += 1
            right -= 1
        return True

