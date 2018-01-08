"""
Add Two Numbers II
@ Linked List + Recursion: To avoid reverse origin list, we can use recursion.
"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1, len2 = self.getLen(l1), self.getLen(l2)
        li, carry = self.addHelper(l1, l2, len1, len2)
        if carry:
            head = ListNode(carry)
            head.next = li
            return head
        return li

    def addHelper(self, l1, l2, len1, len2):
        if not l1:
            return l2, 0
        if not l2:
            return l1, 0
        if len2 > len1:
            return self.addHelper(l2, l1, len2, len1)

        if len1 > len2:
            li, carry = self.addHelper(l1.next, l2, len1 - 1, len2)
            val = l1.val + carry
            l1.val = val % 10
            l1.next = li
            return l1, val / 10
        if len1 == len2:
            li, carry = self.addHelper(l1.next, l2.next, len1 - 1, len2 - 1)
            val = l1.val + l2.val + carry
            head = ListNode(val % 10)
            head.next = li
            return head, val / 10

    def getLen(self, head):
        res = 0
        while head:
            res += 1
            head = head.next
        return res
