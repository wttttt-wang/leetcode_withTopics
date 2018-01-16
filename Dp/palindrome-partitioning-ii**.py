"""
Palindrome Partitioning II
@ dp: The basic solution is calculate isPalindrome first, and then dp[i] = 1 + dp[j] if s[j + 1: i] isPalindrome.
      The solution below will not calculate and store isPalindrome.
      The key point is for each index i, suppose it as center, and j as radius, then the palindrome is here.
      Note that the palindrome can be both even and odd length.
"""


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [i - 1 for i in range(len(s) + 1)]
        for i in range(len(s)):
            j = 0
            while j <= i and j + i < len(s) and s[i - j] == s[i + j]:  # palindrome of odd length
                dp[j + i + 1] = min(dp[j + i + 1], dp[i - j] + 1)
                j += 1
            j = 1
            while j <= i + 1 and j + i < len(s) and s[i - j + 1] == s[i + j]:  # palindrome of even length
                dp[j + i + 1] = min(dp[j + i + 1], dp[i - j + 1] + 1)
                j += 1
        return dp[-1]

