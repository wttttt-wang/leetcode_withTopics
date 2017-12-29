"""
Merge k Sorted Lists
@ Easy problem in 'Hard' tag. > <
@ For more info, see 'Heap/merge-k-sorted-lists'
@ O(NlogK) time, N is total length of all k lists
"""
from heapq import *


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap, results = [], []
        for l in lists:
            if l:
                heappush(heap, (l.val, l))
        while heap:
            v, n = heappop(heap)
            results.append(v)
            if n.next:
                heappush(heap, (n.next.val, n.next))
        return results


