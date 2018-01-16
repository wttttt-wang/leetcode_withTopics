"""
Russian Doll Envelopes
@ Sort + BinarySearch: The key point is how to sort.
                       (Because of 'greater than', we must sort by height asc when width equals)
                       After sort, the way is almost the same as 'longest-increasing-subsequence'
"""


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        # 1. sort, first by width desc, then by height asc
        envelopes.sort(key=lambda (w, h): (-w, h))
        descArr = []
        for w, h in envelopes:
            self.bsAndInsert(h, descArr)
        return len(descArr)

    def bsAndInsert(self, val, descArr):
        # find the left-most descArr[i] <= val
        if not descArr or val < descArr[-1]:
            descArr.append(val)
            return
        left, right = 0, len(descArr) - 1
        while left < right - 1:
            mid = (right - left) / 2 + left
            if descArr[mid] == val:
                return
            elif descArr[mid] < val:
                right = mid
            else:
                left = mid
        if val >= descArr[left]:
            descArr[left] = val
        elif val >= descArr[right]:
            descArr[right] = val
