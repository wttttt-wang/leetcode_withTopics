"""
Reverse Vowels of a String
@ Two pointers
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        res = list(s)
        left, right = 0, len(res) - 1
        while left < right:
            while left < right and res[left] not in vowels:
                left += 1
            while left < right and res[right] not in vowels:
                right -= 1
            if left < right:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
        return "".join(res)
