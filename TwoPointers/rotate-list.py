"""
Rotate List
@ Two pointers  + Linked List
"""


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        # 1. get length
        length = self.getLen(head)
        k %= length
        if k == 0:
            return head
        former = head
        for i in range(k):
            former = former.next
        latter = head
        while former.next:
            former = former.next
            latter = latter.next
        tmp = latter.next
        latter.next = None
        former.next = head
        return tmp

    def getLen(self, head):
        res = 0
        while head:
            res += 1
            head = head.next
        return res
