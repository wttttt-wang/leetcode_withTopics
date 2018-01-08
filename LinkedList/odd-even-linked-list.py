"""
Odd Even Linked List
@ Linked List
"""


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        odd, even = ListNode(0), ListNode(0)
        odd1, even1 = odd, even
        while head:
            odd1.next = head
            odd1 = odd1.next
            head = head.next
            if head:
                even1.next = head
                even1 = even1.next
                head = head.next
        odd1.next = even.next
        even1.next = None
        return odd.next
