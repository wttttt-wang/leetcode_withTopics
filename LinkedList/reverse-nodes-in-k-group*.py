"""
Reverse Nodes in k-Group
@ Linked List
"""


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        dummy = ListNode(0)
        tmp = dummy
        while head:
            h, t, n = self.reverseK(head, k)
            tmp.next = h
            tmp = t
            head = n
        return dummy.next

    def reverseK(self, head, k):
        # 1. get length, return directly if length < k
        cnt, cntTmp = 0, head
        while cntTmp:
            cnt += 1
            cntTmp = cntTmp.next
        if cnt < k:
            return head, None, None
        cnt, tmpTail, tmp = 0, None, head
        while cnt < k:
            tmpNext = tmp.next
            tmp.next = tmpTail
            tmpTail = tmp
            tmp = tmpNext
            cnt += 1
        return tmpTail, head, tmp
