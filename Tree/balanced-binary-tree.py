"""
Balanced Binary Tree
@ Tree + DFS
"""


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)[1]

    def helper(self, root):
        if not root:
            return 0, True
        l, lf = self.helper(root.left)
        if not lf:
            return l, False
        r, rf = self.helper(root.right)
        return max(l, r) + 1, rf and abs(l - r) <= 1
