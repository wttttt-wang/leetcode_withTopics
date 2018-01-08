"""
Repeated DNA Sequences
@ Hash
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) < 10:
            return []
        results = []
        chars = [s[i] for i in range(10)]
        occurs = {"".join(chars): 1}
        for i in range(10, len(s)):
            chars.pop(0)
            chars.append(s[i])
            tmp = "".join(chars)
            if tmp not in occurs:
                occurs[tmp] = 1
            elif occurs[tmp]:
                results.append(tmp)
                occurs[tmp] = 0
        return results

