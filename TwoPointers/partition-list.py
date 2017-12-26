"""
Partition List
@ Two pointers: Nothing special
"""


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return
        left, right = ListNode(0), ListNode(0)
        tmpLeft, tmpRight = left, right
        tmp = head
        while tmp:
            if tmp.val < x:
                tmpLeft.next = tmp
                tmpLeft = tmpLeft.next
            else:
                tmpRight.next = tmp
                tmpRight = tmpRight.next
            tmp = tmp.next
        tmpRight.next = None
        tmpLeft.next = right.next
        return left.next
