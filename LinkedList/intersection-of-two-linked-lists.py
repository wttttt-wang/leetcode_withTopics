"""
Intersection of Two Linked Lists
@ Linked List
"""


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        tailB = self.getTail(headB)
        tailB.next = headA

        slow, fast = headB, headB
        flag = False
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                flag = True
                break
        if not flag:
            tailB.next = None
            return None

        slow = headB
        while slow != fast:
            slow, fast = slow.next, fast.next
        tailB.next = None
        return slow

    def getTail(self, head):
        while head.next:
            head = head.next
        return head

