"""
Kth Smallest Element in a Sorted Matrix
@ Heap: O(K * logM) time, almost the same as 'heap/find-k-pairs-with-smallest-sums'
@ Also see 'BinarySearch/Kth Smallest Element in a Sorted Matrix'
"""


from heapq import *


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0] or k <= 0:
            return None
        m, n = len(matrix), len(matrix[0])
        if k > m * n:
            return None
        heap = []
        for i in range(m):
            heappush(heap, (matrix[i][0], i, 0))
        cnt = 1
        while heap and cnt < k:
            _, i, j = heappop(heap)
            if j + 1 < n:
                heappush(heap, (matrix[i][j + 1], i, j + 1))
            cnt += 1
        return heappop(heap)[0] if heap else None

