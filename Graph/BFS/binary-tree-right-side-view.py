"""
Binary Tree Right Side View
@ BFS
"""


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        results = []
        queue = [root]
        while queue:
            size = len(queue)
            results.append(queue[-1].val)
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return results
