"""
Linked List Cycle II
@ Two pointers + Linked list
"""


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        slow, fast = head, head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if not flag:
            return
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow