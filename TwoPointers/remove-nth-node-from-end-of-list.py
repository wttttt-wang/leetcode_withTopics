"""
Remove Nth Node From End of List
@ Explanation: One-pass solution. Using Two pointers.
@ Corner case: remove head
"""


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        former = head
        for i in range(n):
            former = former.next
        latter = head
        if not former:
            return head.next   # corner case
        while former and former.next:
            former = former.next
            latter = latter.next
        latter.next = latter.next.next
        return head
