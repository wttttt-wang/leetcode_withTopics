"""
Reverse Linked List II
@ Linked List: The key point is to use dummy > <
"""


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next, before = head, dummy
        for i in range(m - 1):
            before = before.next
        h = self.reverseK(before.next, n - m + 1)
        before.next = h
        return dummy.next

    def reverseK(self, head, k):
        tail = head
        tmpTail, tmp = None, head
        for i in range(k):
            tn = tmp.next
            tmp.next = tmpTail
            tmpTail = tmp
            tmp = tn
        tail.next = tmp
        return tmpTail
