"""
Binary Tree Maximum Path Sum
@ Tree + DFS
"""


class Solution(object):
    _res = 0

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self._res = -sys.maxint
        self.helper(root)
        return self._res

    def helper(self, root):
        if not root:
            return 0
        l, r = self.helper(root.left), self.helper(root.right)
        # Attention: always need to compare with 0 first
        self._res = max(self._res, (l if l > 0 else 0) + (r if r > 0 else 0) + root.val)
        return max(l, r, 0) + root.val
