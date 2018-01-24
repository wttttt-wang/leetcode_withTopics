"""
Find All Anagrams in a String
@ Sliding Window + Hash: 1. go ahead right, and update cnt when occurs[ind(right)] > 0
                         2. when right - left == len(target) --> left += 1, and update cnt when occurs[ind(left)] > -1
@ Note: Try to use just one cnt array instead of two!
"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p or len(p) > len(s):
            return []
        results, occurs = [], [0] * 26
        for c in p:
            occurs[ord(c) - ord('a')] += 1
        left, right, cnt = 0, 0, len(p)
        while right < len(s):
            ind = ord(s[right]) - ord('a')
            occurs[ind] -= 1
            if occurs[ind] >= 0:
                cnt -= 1
            right += 1
            if cnt == 0:
                results.append(left)
            if right - left == len(p):   # only update left when reaches target length
                ind2 = ord(s[left]) - ord('a')
                occurs[ind2] += 1
                if occurs[ind2] >= 1:
                    cnt += 1
                left += 1
        return results

