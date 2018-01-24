"""
Symmetric Tree
@ Tree + DFS
"""


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left:
            return True if not right else False
        if not right or left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
