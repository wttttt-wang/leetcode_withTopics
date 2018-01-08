"""
Remove Duplicates from Sorted List
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
        formerVal = head.val - 1
        dummy = ListNode(0)
        tmp = dummy
        while head:
            if head.val != formerVal:
                tmp.next = head
                tmp = tmp.next
                formerVal = head.val
            head = head.next
        tmp.next = None
        return dummy.next


