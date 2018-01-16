"""
Find Largest Value in Each Tree Row
@ BFS(Level-order traversal): Nothing special.
"""


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        results, queue = [], [root]
        while queue:
            size = len(queue)
            tmp = -sys.maxint
            for i in range(size):
                node = queue.pop(0)
                tmp = max(tmp, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(tmp)
        return results
