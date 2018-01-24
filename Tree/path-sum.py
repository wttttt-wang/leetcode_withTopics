"""
Path Sum
@ Tree + DFS
@ Note that a leaf is a node without left child 'and' right child.
"""


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        occurs = self.helper(root)
        return sum in occurs

    def helper(self, root):
        if not root:
            return set()
        if not root.left and not root.right:
            return {root.val}
        res = set()
        l, r = self.helper(root.left), self.helper(root.right)
        for k in l:
            res.add(k + root.val)
        for k in r:
            res.add(k + root.val)
        return res
