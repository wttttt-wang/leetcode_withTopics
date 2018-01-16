"""
Minimum Depth of Binary Tree
@ BFS + Tree
@ Note that is the height to "leaf".
"""


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res, queue = 0, [root]
        while queue:
            size = len(queue)
            res += 1
            for i in range(size):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return res  # come to leaf
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
