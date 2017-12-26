"""
Remove Duplicate Letters
@ Greedy: Always select the minimum selectable letter.
          1. selectable: at least one left for each required letter.
          2. minimum: using recursion to do this.
"""


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        # greedy, time complexity = O(26 * n) = O(n)
        pos = 0   # the pos of the current smallest alpha
        cntStr = [0 for _ in range(26)]
        for val in s:
            cntStr[ord(val) - ord('a')] += 1
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            cntStr[ord(s[i]) - ord('a')] -= 1
            if cntStr[ord(s[i]) - ord('a')] == 0:
                break
        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ""))
