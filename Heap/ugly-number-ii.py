"""
Ugly Number II
@ Heap: O(NlogN) time, O(N) space
@ Note: Do not forget 'visited'
@ Note: For more efficient solution, see 'dp/ugly-number-ii'
"""


from heapq import *


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap, visited = [1], set()
        base = [2, 3, 5]
        for i in range(n - 1):
            val = heappop(heap)
            for v in base:
                tmp = v * val
                if tmp not in visited:
                    heappush(heap, tmp)
                    visited.add(tmp)
        return heappop(heap)
