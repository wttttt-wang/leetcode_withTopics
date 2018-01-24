"""
Validate Binary Search Tree
@ Tree(Binary Search Tree) + DFS
"""


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, -sys.maxint, sys.maxint)

    def helper(self, root, down, up):
        if not root:
            return True
        if root.val <= down or root.val >= up:
            return False
        if not self.helper(root.left, down, root.val):
            return False
        return self.helper(root.right, root.val, up)
