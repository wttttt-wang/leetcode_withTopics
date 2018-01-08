"""
Reverse Linked List
@ Linked List
"""


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = None
        while head:
            tmpNext = head.next
            head.next = tail
            tail, head = head, tmpNext
        return tail