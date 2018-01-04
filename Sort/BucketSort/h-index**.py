"""
H-Index
@ Bucket Sort: For that the result will not bigger than len(cita
@ O(N) time & O(N) space
@ For solution with O(1) space & O(NlogN) time, refer to 'Sort/h-index'
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        buckets = [0] * (len(citations) + 1)
        for val in citations:
            if val >= len(buckets):
                buckets[-1] += 1
            else:
                buckets[val] += 1
        cnt = 0
        for i in range(len(buckets) - 1, -1, -1):
            cnt += buckets[i]
            if cnt >= i:
                return i
        return 0

