"""
Remove Nth Node From End of List
@ Some tricky
@ Explanation: One-pass solution. Using Two pointers.
"""


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1, p2 = head, head
        # 1. p2 go n steps
        for _ in range(n):
            if not p2.next:  # as n is always valid, so it's to remove the first node
                return head.next
            p2 = p2.next
        # 2. find the former node of the node to be deleted
        while p2.next:
            p2 = p2.next
            p1 = p1.next
        p1.next = p1.next.next
        return head

