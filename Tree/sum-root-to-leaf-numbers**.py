"""
Sum Root to Leaf Numbers
@ Tree + DFS: The key point is to sum from up to bottom instead of bottom to up.
"""


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)

    def helper(self, root, curSum):
        if not root:
            return curSum
        if not root.left and not root.right:
            return curSum * 10 + root.val
        res = 0
        if root.left:
            res += self.helper(root.left, curSum * 10 + root.val)
        if root.right:
            res += self.helper(root.right, curSum * 10 + root.val)
        return res
