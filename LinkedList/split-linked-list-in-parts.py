"""
Split Linked List in Parts
@ Linked List
"""


class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if k <= 0:
            return []
        results = [None] * k
        length = self.getLen(head)
        for i in range(k):
            cnt = length / k + (1 if i < length % k else 0)
            if cnt <= 0:
                return results
            results[i] = head
            for j in range(cnt - 1):
                head = head.next
            tmp = head.next
            head.next = None
            head = tmp
        return results

    def getLen(self, head):
        res = 0
        while head:
            res += 1
            head = head.next
        return res
