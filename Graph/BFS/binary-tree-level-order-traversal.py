"""
Binary Tree Level Order Traversal
@ BFS + Tree: Nothing special.
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        results = []
        queue = [root]
        while queue:
            size, res = len(queue), []
            for i in range(size):
                node = queue.pop(0)
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(res)
        return results
