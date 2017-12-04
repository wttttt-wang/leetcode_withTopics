"""
Merge k Sorted Lists
@ Easy problem in 'Hard' tag. > <
@ For more info, see 'Heap/merge-k-sorted-lists'
"""


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        # solution2: divide and conquer
        return self.mergeHelper(lists)

    def mergeHelper(self, lists):
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) / 2
        left, right = self.mergeHelper(lists[:mid]), self.mergeHelper(lists[mid:])
        resHead = ListNode(0)
        tmp = resHead
        while left and right:
            if left.val < right.val:
                tmp.next = left
                left = left.next
            else:
                tmp.next = right
                right = right.next
            tmp = tmp.next
        if left:
            tmp.next = left
        elif right:
            tmp.next = right
        return resHead.next

