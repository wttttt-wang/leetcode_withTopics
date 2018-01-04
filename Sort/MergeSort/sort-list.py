"""
Sort List
@ Merge Sort
@ Note: Need to split left & right part.
"""


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # merge sort
        # 1. find mid & recursion
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        left, right = head, slow.next
        slow.next = None  # Do not forget to split left & right
        left, right = self.sortList(left), self.sortList(right)
        # 2. merge
        dummy = ListNode(0)
        tmp = dummy
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
        return dummy.next
