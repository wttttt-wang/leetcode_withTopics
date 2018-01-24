"""
House Robber III
@ Tree + DFS
"""


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a, b = self.helper(root)
        return max(a, b)

    def helper(self, root):
        if not root:
            return 0, 0
        lnt, lt = self.helper(root.left)
        rnt, rt = self.helper(root.right)
        return max(lt, lnt) + max(rt, rnt), root.val + lnt + rnt
