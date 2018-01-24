"""
Populating Next Right Pointers in Each Node
@ Tree: O(1) space --> when relationship of prev-level is constructed, we can simply use this.
                       Also note that the tree is a perfect binary tree.
"""


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        prev, cur = root, root.left  # prev means prev-level
        while cur:
            tmp = cur
            cur.next = prev.right
            prev, cur = prev.next, cur.next
            while prev:
                cur.next = prev.left
                cur = cur.next
                cur.next = prev.right
                cur, prev = cur.next, prev.next
            prev, cur = tmp, tmp.left
