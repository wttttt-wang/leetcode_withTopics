"""
Add Two Numbers
@ Attention: 1. do not forget the last carry 2. do not forget the left linked list.
"""


class Solution(object):
    def addTwoNumbers(self, p1, p2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        tmp = head
        flag = 0
        while p1 and p2:
            val = flag + p1.val + p2.val
            if val >= 10:
                val -= 10
                flag = 1
            else:
                flag = 0
            tmp.next = ListNode(val)
            tmp = tmp.next
            p1 = p1.next
            p2 = p2.next
        if p1:
            tmp, flag = self.tail(p1, flag, tmp)
        elif p2:
            tmp, flag = self.tail(p2, flag, tmp)
        if flag:
            tmp.next = ListNode(1)
        return head.next

    def tail(self, p1, flag, tmp):
        while p1:
            val = flag + p1.val
            if val >= 10:
                val -= 10
                flag = 1
            else:
                flag = 0
            tmp.next = ListNode(val)
            tmp = tmp.next
            p1 = p1.next
        return tmp, flag

