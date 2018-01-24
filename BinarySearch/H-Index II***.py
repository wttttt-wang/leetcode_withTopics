"""
H-Index II
@ Binary Search: The key point is left-most instead of right-most!!!
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        # find the left-most ind where len - ind <= citations[ind]
        left, right = 0, len(citations) - 1
        while left < right - 1:
            mid = (right - left) / 2 + left
            if len(citations) - mid <= citations[mid]:
                right = mid
            else:
                left = mid
        if citations[left] >= len(citations) - left:
            return len(citations) - left
        if citations[right] >= len(citations) - right:
            return len(citations) - right
        return 0
