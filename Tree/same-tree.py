"""
Same Tree
@ Tree + DFS
"""


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p:
            return True if not q else False
        if not q or p.val != q.val:
            return False
        return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
