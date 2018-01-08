"""
Reorder List
@ Linked List
"""


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        left, right = head, slow.next
        slow.next = None  # split

        # 2. reverse right part
        tail, tmp = None, right
        while tmp:
            tmpNext = tmp.next
            tmp.next = tail
            tail, tmp = tmp, tmpNext
        right = tail
        dummy = ListNode(0)
        tmp = dummy
        while left and right:
            tmp.next = left
            left, tmp = left.next, tmp.next
            tmp.next = right
            right, tmp = right.next, tmp.next
        if left:
            tmp.next = left
        elif right:
            tmp.next = right
