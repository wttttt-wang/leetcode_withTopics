"""
Remove Linked List Elements
@ Linked List
@ Note that the tail should point to None!!!
"""


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return
        dummy = ListNode(0)
        tmp = dummy
        while head:
            if head.val != val:
                tmp.next = head
                tmp = tmp.next
            head = head.next
        tmp.next = None   # Attention: This is really important!!!
        return dummy.next
