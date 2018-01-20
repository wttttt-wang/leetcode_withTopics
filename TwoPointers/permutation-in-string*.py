"""
Permutation in String
@ Two pointers(Sliding window): The key point is to use cnt array.
"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1:
            return True
        if not s2:
            return False
        hitCnt = 0
        tarArr, srcArr = [0] * 26, [0] * 26
        for c in s1:
            srcArr[ord(c) - ord('a')] += 1
        left, right = 0, 0
        while right < len(s2):
            if hitCnt == len(s1):
                return True
            ind = ord(s2[right]) - ord('a')
            if tarArr[ind] < srcArr[ind]:
                tarArr[ind] += 1
                hitCnt += 1
            else:
                while left < right and s2[left] != s2[right]:
                    tarArr[ord(s2[left]) - ord('a')] -= 1
                    hitCnt -= 1
                    left += 1
                left += 1
            right += 1
        return hitCnt == len(s1)
