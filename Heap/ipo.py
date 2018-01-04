"""
IPO
@ Heap + Greedy: greedy is to put the current optional(Ci <= curr) project with maximum profit.
                 To update optional projects to heap, I sort the capital first. Instead, we can also use another heap.
@ Note: 'The answer is guaranteed to fit in a 32-bit signed integer.' in the note of this problem.
         But the point is will u ask this?
"""


from heapq import *


class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        if k <= 0 or not Profits:
            return 0
        curr, heap, cnt = W, [], 0
        sortedC, indC = sorted(enumerate(Capital), key=lambda x: x[1]), 0
        while cnt < k:
            # update heap
            while indC < len(sortedC) and sortedC[indC][1] <= curr:
                heappush(heap, -Profits[sortedC[indC][0]])
                indC += 1
            if not heap:
                return curr
            curr -= heappop(heap)
            cnt += 1
        return curr

