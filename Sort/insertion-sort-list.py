"""
Insertion Sort List
@ Sort + Linked list
"""


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        dummy = ListNode(0)
        while head:
            tmp = dummy.next
            former = dummy
            while tmp and head.val > tmp.val:
                tmp = tmp.next
                former = former.next
            tmpNode = head.next
            head.next = former.next
            former.next = head
            head = tmpNode
        return dummy.next
