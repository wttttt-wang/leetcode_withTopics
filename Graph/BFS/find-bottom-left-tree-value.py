"""
Find Bottom Left Tree Value
@ BFS: Almost the same as 'Graph/BFS/binary-tree-right-side-view'
@ DFS is also doable.
"""


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        queue = [root]
        res = None
        while queue:
            size = len(queue)
            res = queue[0].val
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

