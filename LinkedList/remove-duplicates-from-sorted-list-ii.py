"""
Remove Duplicates from Sorted List II
@ Linked List
"""


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        dummy = ListNode(0)
        tmp = dummy
        formerVal = head.val - 1
        while head:
            if head.val != formerVal and (not head.next or head.next.val != head.val):
                tmp.next = head
                tmp = tmp.next
            formerVal = head.val
            head = head.next
        tmp.next = None
        return dummy.next

