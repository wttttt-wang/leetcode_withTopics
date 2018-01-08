"""
Convert Sorted List to Binary Search Tree
@ Linked List + DFS
"""


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        # 1. find median
        medianBefore = self.getMedian(head)
        median = medianBefore.next
        res = TreeNode(median.val)
        medianBefore.next = None
        res.left = self.sortedListToBST(head)
        res.right = self.sortedListToBST(median.next)
        return res

    def getMedian(self, head):
        slow, fast = head, head.next
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        return slow
