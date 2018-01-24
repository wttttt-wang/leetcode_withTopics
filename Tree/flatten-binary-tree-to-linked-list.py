"""
Flatten Binary Tree to Linked List
@ Tree + DFS
"""


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)

    def helper(self, root):
        if not root:
            return None, None
        l, r = root.left, root.right
        tail = root
        if root.left:
            root.left = None
            root.right, tail = self.helper(l)
        if r:
            tail.right, tail = self.helper(r)
        return root, tail

