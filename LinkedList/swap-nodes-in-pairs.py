"""
Swap Nodes in Pairs
@ Linked List
"""


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        dummy = ListNode(0)
        tmp = dummy
        while head and head.next:
            tmp.next = head.next
            tmp2 = head.next.next
            head.next.next = head
            tmp = head
            head = tmp2
        tmp.next = head
        return dummy.next

