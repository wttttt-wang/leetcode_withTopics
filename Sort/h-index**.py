"""
H-Index
@ Sort: O(NlogN) time & O(1) space
@ For solution with O(N) space & O(N) time, refer to 'Sort/BucketSort/h-index'
@ Update: After sort, we can use binary search to find the result, refer to 'BinarySearch/H-Index II'
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        res = 0
        for i in range(len(citations) - 1, -1, -1):
            if citations[i] <= len(citations) - i:
                res = max(res, citations[i])
            else:
                res = max(res, len(citations) - i)
        return res

