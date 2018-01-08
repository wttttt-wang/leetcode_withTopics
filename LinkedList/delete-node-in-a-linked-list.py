"""
Delete Node in a Linked List
@ Linked List
"""


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node:
            return
        node.val = node.next.val
        node.next = node.next.next
