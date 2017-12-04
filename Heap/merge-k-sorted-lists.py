"""
Merge k Sorted Lists
@ Easy problem in 'Hard' tag. > <
@ For more info, see 'Heap/merge-k-sorted-lists'
"""
from heapq import *


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        # 1. initialize heap
        for h in lists:
            if h:
                heappush(heap, (h.val, h))
        resultHead = ListNode(0)
        tmp = resultHead
        while heap:
            _, node = heappop(heap)
            tmp.next = node
            tmp = tmp.next
            if node.next:
                heappush(heap, (node.next.val, node.next))
        return resultHead.next
