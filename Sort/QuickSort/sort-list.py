"""
Sort List
@ Quick Sort
@ Note: Need to split left & right part.
"""


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(head)[0]

    def helper(self, head):
        if not head or not head.next:
            return head, head
        # quick sort
        left, right, equal = ListNode(0), ListNode(0), ListNode(0)
        leftTmp, rightTmp, equalTmp = left, right, equal
        pivot = head.val
        while head:
            if head.val == pivot:
                equalTmp.next = head
                equalTmp = equalTmp.next
            elif head.val < pivot:
                leftTmp.next = head
                leftTmp = leftTmp.next
            else:
                rightTmp.next = head
                rightTmp = rightTmp.next
            head = head.next
        # split!
        leftTmp.next, equalTmp.next, rightTmp.next = None, None, None
        left, leftTail = self.helper(left.next)
        right, rightTail = self.helper(right.next)
        dummy = ListNode(0)
        resTail = dummy
        if left:
            resTail.next = left
            resTail = leftTail
        if equal:
            resTail.next = equal.next
            resTail = equalTmp
        if right:
            resTail.next = right
            resTail = rightTail
        return dummy.next, resTail

