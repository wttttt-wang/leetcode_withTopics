"""
Count Complete Tree Nodes
@ Tree + Recursion: O(h ^ 2) time
"""


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        hleft, hright = self.getHeight(root.left, True), self.getHeight(root.right, False)
        if hleft == hright:
            return 2 ** (hleft + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getHeight(self, root, isLeft):
        res = 0
        while root:
            res += 1
            if isLeft:
                root = root.left
            else:
                root = root.right
        return res
