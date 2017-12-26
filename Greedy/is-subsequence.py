"""
Is Subsequence
@ Greedy + Two pointers
@ O(N + M) time
@ Follow up: What if there are lots of incoming S? --> Obviously we should do pre-processing for S. The same greedy idea
             as this, we need to find the leftmost matching char for each char in T. So:
             1. get occurs index for each char.
             2. for each char in S, do binary search (find the smallest index which larger than current given index)
"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False
        ps, pt = 0, 0
        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
                pt += 1
            else:
                pt += 1
        return ps == len(s)

