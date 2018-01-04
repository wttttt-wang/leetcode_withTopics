"""
Find K Pairs with Smallest Sums
"""


from heapq import *


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if k <= 0 or not nums1 or not nums2:
            return []
        results = []
        m, n = len(nums1), len(nums2)   # assume m < n, O(klogm) time
        if m > n:
            return [[v2, v1] for v1, v2 in self.kSmallestPairs(nums2, nums1, k)]
        heap = []
        for i in range(m):
            heappush(heap, (nums1[i] + nums2[0], i, 0))
        while heap and len(results) < k:
            val, i, j = heappop(heap)
            results.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return results

